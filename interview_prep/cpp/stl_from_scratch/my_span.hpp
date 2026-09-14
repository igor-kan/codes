// Minimal std::span: a non-owning view over contiguous memory.
#pragma once
#include <cstddef>
#include <stdexcept>

namespace mystl {

template <typename T>
class span {
  public:
    constexpr span() noexcept = default;
    constexpr span(T *data, std::size_t size) noexcept : data_(data), size_(size) {}
    template <std::size_t N>
    constexpr span(T (&array)[N]) noexcept : data_(array), size_(N) {}

    constexpr std::size_t size() const noexcept { return size_; }
    constexpr bool empty() const noexcept { return size_ == 0; }
    constexpr T *data() const noexcept { return data_; }
    constexpr T &operator[](std::size_t i) const { return data_[i]; }
    constexpr T &front() const { return data_[0]; }
    constexpr T &back() const { return data_[size_ - 1]; }
    constexpr T *begin() const noexcept { return data_; }
    constexpr T *end() const noexcept { return data_ + size_; }
    constexpr span subspan(std::size_t offset, std::size_t count) const {
        if (offset + count > size_) throw std::out_of_range("subspan");
        return span(data_ + offset, count);
    }

  private:
    T *data_ = nullptr;
    std::size_t size_ = 0;
};

}  // namespace mystl
