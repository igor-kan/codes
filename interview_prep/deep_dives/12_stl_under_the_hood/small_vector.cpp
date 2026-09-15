// Small-buffer-optimized vector (inline storage until it grows).
#include <cstddef>
#include <iostream>
#include <new>
#include <utility>

template <typename T, std::size_t N>
class SmallVector {
  public:
    SmallVector() = default;
    ~SmallVector() { clear(); if (heap_) ::operator delete(heap_); }
    SmallVector(const SmallVector &) = delete;
    SmallVector &operator=(const SmallVector &) = delete;

    void push_back(const T &value) {
        if (size_ < N) { new (inline_ + size_) T(value); }
        else {
            if (!heap_) grow();
            new (heap_ + size_) T(value);
        }
        ++size_;
    }

    std::size_t size() const { return size_; }
    bool on_heap() const { return heap_ != nullptr; }
    const T &operator[](std::size_t i) const { return data()[i]; }

  private:
    T *data() { return heap_ ? heap_ : reinterpret_cast<T *>(inline_); }
    const T *data() const { return heap_ ? heap_ : reinterpret_cast<const T *>(inline_); }
    void grow() {
        heap_ = static_cast<T *>(::operator new(2 * N * sizeof(T)));
        for (std::size_t i = 0; i < N; ++i) { new (heap_ + i) T(data()[i]); data()[i].~T(); }
    }
    void clear() { for (std::size_t i = 0; i < size_ && i < N; ++i) data()[i].~T(); }

    alignas(T) unsigned char inline_[sizeof(T) * N];
    T *heap_ = nullptr;
    std::size_t size_ = 0;
};

int main() {
    SmallVector<int, 4> small;
    for (int i = 0; i < 3; ++i) small.push_back(i);
    SmallVector<int, 4> big;
    for (int i = 0; i < 10; ++i) big.push_back(i);
    std::cout << "small on_heap=" << small.on_heap() << " big on_heap=" << big.on_heap()
              << " big[9]=" << big[9] << '\n';
    return 0;
}
