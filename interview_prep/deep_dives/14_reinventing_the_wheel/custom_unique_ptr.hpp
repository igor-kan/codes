// From-scratch unique_ptr with custom deleter support.
#pragma once
#include <memory>
#include <utility>

namespace wheel {

template <typename T, typename Deleter = std::default_delete<T>>
class UniquePtr {
  public:
    UniquePtr() = default;
    explicit UniquePtr(T *ptr) : ptr_(ptr) {}
    UniquePtr(T *ptr, Deleter deleter) : ptr_(ptr), deleter_(std::move(deleter)) {}
    UniquePtr(const UniquePtr &) = delete;
    UniquePtr &operator=(const UniquePtr &) = delete;
    UniquePtr(UniquePtr &&other) noexcept
        : ptr_(std::exchange(other.ptr_, nullptr)), deleter_(std::move(other.deleter_)) {}
    UniquePtr &operator=(UniquePtr &&other) noexcept {
        if (this != &other) { reset(); ptr_ = std::exchange(other.ptr_, nullptr); deleter_ = std::move(other.deleter_); }
        return *this;
    }
    ~UniquePtr() { reset(); }

    void reset(T *ptr = nullptr) { if (ptr_) deleter_(ptr_); ptr_ = ptr; }
    T *release() noexcept { return std::exchange(ptr_, nullptr); }
    T *get() const noexcept { return ptr_; }
    T &operator*() const { return *ptr_; }
    T *operator->() const noexcept { return ptr_; }
    explicit operator bool() const noexcept { return ptr_ != nullptr; }

  private:
    T *ptr_ = nullptr;
    Deleter deleter_{};
};

template <typename T, typename... Args>
UniquePtr<T> makeUnique(Args &&...args) {
    return UniquePtr<T>(new T(std::forward<Args>(args)...));
}

}  // namespace wheel
