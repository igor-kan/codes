// A from-scratch dynamic array with move semantics and iterators.
#pragma once
#include <cstddef>
#include <stdexcept>
#include <utility>

namespace wheel {

template <typename T>
class Vector {
  public:
    Vector() = default;
    explicit Vector(std::size_t n) : data_(new T[n]()), size_(n), cap_(n) {}
    Vector(const Vector &other) { reserve(other.size_); for (const auto &v : other) push_back(v); }
    Vector(Vector &&other) noexcept
        : data_(std::exchange(other.data_, nullptr)),
          size_(std::exchange(other.size_, 0)),
          cap_(std::exchange(other.cap_, 0)) {}
    ~Vector() { delete[] data_; }

    Vector &operator=(Vector other) { swap(other); return *this; }
    void swap(Vector &other) noexcept { std::swap(data_, other.data_); std::swap(size_, other.size_); std::swap(cap_, other.cap_); }

    void push_back(const T &value) {
        if (size_ == cap_) reserve(cap_ ? cap_ * 2 : 1);
        data_[size_++] = value;
    }
    void pop_back() { if (size_) --size_; }
    T &operator[](std::size_t i) { return data_[i]; }
    const T &operator[](std::size_t i) const { return data_[i]; }
    T &at(std::size_t i) { if (i >= size_) throw std::out_of_range("Vector::at"); return data_[i]; }
    std::size_t size() const noexcept { return size_; }
    std::size_t capacity() const noexcept { return cap_; }
    bool empty() const noexcept { return size_ == 0; }
    T *begin() noexcept { return data_; }
    T *end() noexcept { return data_ + size_; }
    const T *begin() const noexcept { return data_; }
    const T *end() const noexcept { return data_ + size_; }

    void reserve(std::size_t n) {
        if (n <= cap_) return;
        T *fresh = new T[n];
        for (std::size_t i = 0; i < size_; ++i) fresh[i] = std::move(data_[i]);
        delete[] data_;
        data_ = fresh; cap_ = n;
    }

  private:
    T *data_ = nullptr;
    std::size_t size_ = 0, cap_ = 0;
};

}  // namespace wheel
