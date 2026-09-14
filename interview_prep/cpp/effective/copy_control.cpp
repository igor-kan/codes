// Effective C++ -- handle copy construction, assignment and destruction.
#include <cstddef>
#include <iostream>
#include <string>

class String {
  public:
    explicit String(const char *text)
        : size_(std::char_traits<char>::length(text)), data_(new char[size_ + 1]) {
        std::char_traits<char>::copy(data_, text, size_ + 1);
    }
    String(const String &other) : size_(other.size_), data_(new char[size_ + 1]) {
        std::char_traits<char>::copy(data_, other.data_, size_ + 1);
    }
    String &operator=(const String &other) {
        String copy(other);
        swap(copy);
        return *this;
    }
    ~String() { delete[] data_; }
    void swap(String &other) noexcept {
        std::swap(data_, other.data_);
        std::swap(size_, other.size_);
    }
    std::size_t size() const noexcept { return size_; }
    const char *c_str() const noexcept { return data_; }

  private:
    std::size_t size_;
    char *data_;
};

int main() {
    String a("hello");
    String b = a;
    b = a;
    std::cout << a.c_str() << ' ' << b.size() << '\n';
    return 0;
}
