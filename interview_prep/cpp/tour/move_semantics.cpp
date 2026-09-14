// A Tour of C++ -- move semantics and rule of five.
#include <iostream>
#include <utility>
#include <vector>

class Buffer {
  public:
    explicit Buffer(std::size_t n) : data_(new int[n]), size_(n) {}
    ~Buffer() { delete[] data_; }
    Buffer(const Buffer &other) : data_(new int[other.size_]), size_(other.size_) {
        std::copy(other.data_, other.data_ + size_, data_);
    }
    Buffer(Buffer &&other) noexcept
        : data_(std::exchange(other.data_, nullptr)), size_(std::exchange(other.size_, 0)) {}
    Buffer &operator=(Buffer other) { swap(other); return *this; }
    void swap(Buffer &other) noexcept { std::swap(data_, other.data_); std::swap(size_, other.size_); }
    std::size_t size() const { return size_; }

  private:
    int *data_;
    std::size_t size_;
};

int main() {
    Buffer original(1024);
    Buffer moved(std::move(original));
    std::cout << "original=" << original.size() << " moved=" << moved.size() << '\n';
    return 0;
}
