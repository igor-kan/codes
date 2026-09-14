// Minimal std::string reimplementation.
#pragma once
#include <cstddef>
#include <cstring>
#include <utility>

namespace mystl {

class string {
  public:
    string() = default;
    string(const char *s) { assign(s, std::strlen(s)); }
    string(const string &other) { assign(other.data_, other.size_); }
    string(string &&other) noexcept
        : data_(other.data_), size_(other.size_), cap_(other.cap_) {
        other.data_ = nullptr; other.size_ = other.cap_ = 0;
    }
    ~string() { delete[] data_; }

    string &operator=(string other) { swap(other); return *this; }
    void swap(string &other) noexcept {
        std::swap(data_, other.data_); std::swap(size_, other.size_); std::swap(cap_, other.cap_);
    }

    void append(const char *s, std::size_t n) {
        if (size_ + n > cap_) reserve(size_ + n);
        std::memcpy(data_ + size_, s, n);
        size_ += n; data_[size_] = '\0';
    }
    string &operator+=(const string &other) { append(other.data_, other.size_); return *this; }
    const char *c_str() const noexcept { return data_ ? data_ : ""; }
    std::size_t size() const noexcept { return size_; }
    bool empty() const noexcept { return size_ == 0; }
    char operator[](std::size_t i) const { return data_[i]; }

  private:
    void assign(const char *s, std::size_t n) {
        reserve(n); std::memcpy(data_, s, n); size_ = n; data_[n] = '\0';
    }
    void reserve(std::size_t n) {
        if (n <= cap_) return;
        char *fresh = new char[n + 1];
        if (data_) { std::memcpy(fresh, data_, size_); delete[] data_; }
        data_ = fresh; cap_ = n;
    }
    char *data_ = nullptr;
    std::size_t size_ = 0, cap_ = 0;
};

inline string operator+(string a, const string &b) { a += b; return a; }

}  // namespace mystl
