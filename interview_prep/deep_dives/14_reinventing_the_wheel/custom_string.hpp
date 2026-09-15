// From-scratch string with SSO-friendly small buffer.
#pragma once
#include <cstddef>
#include <cstring>
#include <utility>

namespace wheel {

class String {
  public:
    String() = default;
    String(const char *text) { assign(text, std::strlen(text)); }
    String(const String &other) { assign(other.data_, other.size_); }
    String(String &&other) noexcept { swap(other); }
    ~String() { delete[] data_; }

    String &operator=(String other) { swap(other); return *this; }
    void swap(String &other) noexcept {
        std::swap(data_, other.data_); std::swap(size_, other.size_); std::swap(cap_, other.cap_);
    }
    String &operator+=(const String &other) { append(other.data_, other.size_); return *this; }

    void append(const char *text, std::size_t n) {
        if (size_ + n > cap_) reserve(size_ + n);
        std::memcpy(data_ + size_, text, n); size_ += n; data_[size_] = '\0';
    }
    const char *c_str() const noexcept { return data_ ? data_ : ""; }
    std::size_t size() const noexcept { return size_; }
    char operator[](std::size_t i) const { return data_[i]; }
    bool operator==(const String &other) const { return size_ == other.size_ && std::memcmp(data_, other.data_, size_) == 0; }

  private:
    void assign(const char *text, std::size_t n) { reserve(n); std::memcpy(data_, text, n); size_ = n; data_[n] = '\0'; }
    void reserve(std::size_t n) {
        if (n <= cap_) return;
        char *fresh = new char[n + 1];
        if (data_) { std::memcpy(fresh, data_, size_); delete[] data_; }
        data_ = fresh; cap_ = n;
    }
    char *data_ = nullptr;
    std::size_t size_ = 0, cap_ = 0;
};

inline String operator+(String a, const String &b) { a += b; return a; }

}  // namespace wheel
