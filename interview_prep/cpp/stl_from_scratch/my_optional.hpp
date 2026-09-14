// Minimal std::optional reimplementation.
#pragma once
#include <new>
#include <stdexcept>
#include <utility>

namespace mystl {

template <typename T>
class optional {
  public:
    optional() = default;
    optional(const T &value) { emplace(value); }
    optional(T &&value) { emplace(std::move(value)); }
    optional(const optional &other) { if (other.has_value_) emplace(other.value_); }
    optional(optional &&other) noexcept { if (other.has_value_) emplace(std::move(other.value_)); }
    ~optional() { reset(); }

    optional &operator=(optional other) { swap(other); return *this; }
    void swap(optional &other) noexcept { std::swap(value_, other.value_); std::swap(has_value_, other.has_value_); }

    template <typename... Args>
    T &emplace(Args &&...args) {
        reset();
        new (&value_) T(std::forward<Args>(args)...);
        has_value_ = true;
        return value_;
    }
    void reset() { if (has_value_) { value_.~T(); has_value_ = false; } }
    bool has_value() const noexcept { return has_value_; }
    explicit operator bool() const noexcept { return has_value_; }
    T &value() { if (!has_value_) throw std::runtime_error("empty optional"); return value_; }
    const T &value() const { if (!has_value_) throw std::runtime_error("empty optional"); return value_; }
    T &operator*() { return value_; }
    T value_or(const T &fallback) const { return has_value_ ? value_ : fallback; }

  private:
    union { T value_; };
    bool has_value_ = false;
};

}  // namespace mystl
