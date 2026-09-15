// From-scratch shared_ptr with a control block and weak support.
#pragma once
#include <atomic>
#include <utility>

namespace wheel {

template <typename T>
class SharedPtr;

template <typename T>
class ControlBlock {
  public:
    explicit ControlBlock(T *ptr) : ptr_(ptr) {}
    void add_shared() noexcept { shared_.fetch_add(1); }
    void add_weak() noexcept { weak_.fetch_add(1); }
    void release_shared() noexcept {
        if (shared_.fetch_sub(1) == 1) { delete ptr_; ptr_ = nullptr; if (weak_.load() == 0) delete this; }
    }
    void release_weak() noexcept { if (weak_.fetch_sub(1) == 1) delete this; }
    T *get() const noexcept { return ptr_; }
    long use_count() const noexcept { return shared_.load(); }

  private:
    T *ptr_;
    std::atomic<long> shared_{1};
    std::atomic<long> weak_{0};
};

template <typename T>
class SharedPtr {
  public:
    SharedPtr() = default;
    explicit SharedPtr(T *ptr) : control_(ptr ? new ControlBlock<T>(ptr) : nullptr) {}
    SharedPtr(const SharedPtr &other) : control_(other.control_) { if (control_) control_->add_shared(); }
    SharedPtr(SharedPtr &&other) noexcept : control_(std::exchange(other.control_, nullptr)) {}
    ~SharedPtr() { if (control_) control_->release_shared(); }

    SharedPtr &operator=(SharedPtr other) noexcept { swap(other); return *this; }
    void swap(SharedPtr &other) noexcept { std::swap(control_, other.control_); }

    T *get() const noexcept { return control_ ? control_->get() : nullptr; }
    T &operator*() const { return *get(); }
    T *operator->() const noexcept { return get(); }
    explicit operator bool() const noexcept { return get() != nullptr; }
    long use_count() const noexcept { return control_ ? control_->use_count() : 0; }

  private:
    ControlBlock<T> *control_ = nullptr;
};

template <typename T, typename... Args>
SharedPtr<T> makeShared(Args &&...args) {
    return SharedPtr<T>(new T(std::forward<Args>(args)...));
}

}  // namespace wheel
