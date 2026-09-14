// Minimal std::shared_ptr with a reference-counted control block.
#pragma once
#include <atomic>
#include <utility>

namespace mystl {

struct control_block {
    std::atomic<long> refs{1};
    virtual void dispose() noexcept = 0;
    virtual ~control_block() = default;
};

template <typename T>
struct control_block_impl final : control_block {
    explicit control_block_impl(T *p) : ptr(p) {}
    void dispose() noexcept override { delete ptr; }
    T *ptr;
};

template <typename T>
class shared_ptr {
  public:
    shared_ptr() = default;
    explicit shared_ptr(T *p) : ptr_(p), cb_(p ? new control_block_impl<T>(p) : nullptr) {}
    shared_ptr(const shared_ptr &other) : ptr_(other.ptr_), cb_(other.cb_) { retain(); }
    shared_ptr(shared_ptr &&other) noexcept : ptr_(other.ptr_), cb_(other.cb_) {
        other.ptr_ = nullptr; other.cb_ = nullptr;
    }
    ~shared_ptr() { release(); }

    shared_ptr &operator=(shared_ptr other) { swap(other); return *this; }
    void swap(shared_ptr &other) noexcept { std::swap(ptr_, other.ptr_); std::swap(cb_, other.cb_); }

    T *get() const noexcept { return ptr_; }
    T &operator*() const { return *ptr_; }
    T *operator->() const noexcept { return ptr_; }
    explicit operator bool() const noexcept { return ptr_ != nullptr; }
    long use_count() const noexcept { return cb_ ? cb_->refs.load() : 0; }

  private:
    void retain() noexcept { if (cb_) cb_->refs.fetch_add(1); }
    void release() noexcept {
        if (cb_ && cb_->refs.fetch_sub(1) == 1) { cb_->dispose(); delete cb_; }
    }
    T *ptr_ = nullptr;
    control_block *cb_ = nullptr;
};

template <typename T, typename... Args>
shared_ptr<T> make_shared(Args &&...args) {
    return shared_ptr<T>(new T(std::forward<Args>(args)...));
}

}  // namespace mystl
