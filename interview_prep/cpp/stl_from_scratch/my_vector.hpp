// Minimal std::vector reimplementation (C++20).
#pragma once
#include <cstddef>
#include <initializer_list>
#include <stdexcept>
#include <utility>

namespace mystl {

template <typename T>
class vector {
  public:
    using iterator = T *;
    using const_iterator = const T *;

    vector() = default;
    vector(std::initializer_list<T> init) { for (const auto &v : init) push_back(v); }
    vector(const vector &other) { reserve(other.size_); for (const auto &v : other) push_back(v); }
    vector(vector &&other) noexcept : data_(other.data_), size_(other.size_), cap_(other.cap_) {
        other.data_ = nullptr; other.size_ = other.cap_ = 0;
    }
    ~vector() { clear(); operator delete(data_); }

    vector &operator=(vector other) { swap(other); return *this; }
    void swap(vector &other) noexcept {
        std::swap(data_, other.data_); std::swap(size_, other.size_); std::swap(cap_, other.cap_);
    }

    void push_back(const T &value) {
        if (size_ == cap_) reserve(cap_ ? cap_ * 2 : 1);
        new (data_ + size_) T(value);
        ++size_;
    }

    void reserve(std::size_t n) {
        if (n <= cap_) return;
        T *fresh = static_cast<T *>(operator new(n * sizeof(T)));
        for (std::size_t i = 0; i < size_; ++i) { new (fresh + i) T(std::move(data_[i])); data_[i].~T(); }
        operator delete(data_);
        data_ = fresh; cap_ = n;
    }

    void clear() { for (std::size_t i = 0; i < size_; ++i) data_[i].~T(); size_ = 0; }
    T &operator[](std::size_t i) { return data_[i]; }
    const T &operator[](std::size_t i) const { return data_[i]; }
    T &at(std::size_t i) { if (i >= size_) throw std::out_of_range("index"); return data_[i]; }
    T &front() { return data_[0]; }
    T &back() { return data_[size_ - 1]; }
    std::size_t size() const noexcept { return size_; }
    bool empty() const noexcept { return size_ == 0; }
    iterator begin() noexcept { return data_; }
    iterator end() noexcept { return data_ + size_; }
    const_iterator begin() const noexcept { return data_; }
    const_iterator end() const noexcept { return data_ + size_; }

  private:
    T *data_ = nullptr;
    std::size_t size_ = 0;
    std::size_t cap_ = 0;
};

}  // namespace mystl
