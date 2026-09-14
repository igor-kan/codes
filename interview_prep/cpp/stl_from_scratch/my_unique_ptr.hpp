// Minimal std::unique_ptr reimplementation.
#pragma once
#include <utility>

namespace mystl {

template <typename T>
class unique_ptr {
  public:
    unique_ptr() = default;
    explicit unique_ptr(T *p) noexcept : ptr_(p) {}
    unique_ptr(const unique_ptr &) = delete;
    unique_ptr &operator=(const unique_ptr &) = delete;
    unique_ptr(unique_ptr &&other) noexcept : ptr_(std::exchange(other.ptr_, nullptr)) {}
    unique_ptr &operator=(unique_ptr &&other) noexcept {
        reset(std::exchange(other.ptr_, nullptr));
        return *this;
    }
    ~unique_ptr() { reset(); }

    void reset(T *p = nullptr) noexcept { delete ptr_; ptr_ = p; }
    T *release() noexcept { return std::exchange(ptr_, nullptr); }
    T *get() const noexcept { return ptr_; }
    T &operator*() const { return *ptr_; }
    T *operator->() const noexcept { return ptr_; }
    explicit operator bool() const noexcept { return ptr_ != nullptr; }

  private:
    T *ptr_ = nullptr;
};

template <typename T, typename... Args>
unique_ptr<T> make_unique(Args &&...args) {
    return unique_ptr<T>(new T(std::forward<Args>(args)...));
}

}  // namespace mystl
