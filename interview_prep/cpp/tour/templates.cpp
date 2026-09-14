// A Tour of C++ -- function and class templates, concepts.
#include <concepts>
#include <iostream>
#include <string>

template <typename T>
concept Addable = requires(T a, T b) { { a + b } -> std::same_as<T>; };

template <Addable T>
T sum(T a, T b) { return a + b; }

template <typename T, std::size_t N>
class FixedBuffer {
  public:
    constexpr std::size_t size() const noexcept { return N; }
    constexpr T &operator[](std::size_t i) { return data_[i]; }
  private:
    T data_[N]{};
};

int main() {
    std::cout << sum(2, 3) << ' ' << sum(std::string("a"), std::string("b")) << '\n';
    FixedBuffer<double, 4> buf;
    buf[0] = 1.5;
    std::cout << "size=" << buf.size() << " first=" << buf[0] << '\n';
    return 0;
}
