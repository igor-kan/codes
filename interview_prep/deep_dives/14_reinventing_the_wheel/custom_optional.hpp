// From-scratch optional.
#pragma once
#include <new>
#include <stdexcept>
#include <utility>

namespace wheel {

template <typename T>
class Optional {
  public:
    Optional() = default;
    Optional(const T &value) { construct(value); }
    Optional(T &&value) { construct(std::move(value)); }
    Optional(const Optional &other) { if (other.has_) construct(other.value_); }
    Optional(Optional &&other) noexcept { if (other.has_) construct(std::move(other.value_)); }
    ~Optional() { reset(); }

    Optional &operator=(Optional other) { swap(other); return *this; }
    void swap(Optional &other) noexcept {
        std::swap(value_, other.value_); std::swap(has_, other.has_);
    }
    void reset() { if (has_) { value_.~T(); has_ = false; } }
    bool has_value() const noexcept { return has_; }
    explicit operator bool() const noexcept { return has_; }
    T &value() { if (!has_) throw std::runtime_error("empty Optional"); return value_; }
    T value_or(const T &fallback) const { return has_ ? value_ : fallback; }
    T &operator*() { return value_; }

  private:
    template <typename U>
    void construct(U &&value) { new (&value_) T(std::forward<U>(value)); has_ = true; }
    union { T value_; };
    bool has_ = false;
};

}  // namespace wheel
