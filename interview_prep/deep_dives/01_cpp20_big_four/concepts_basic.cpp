// C++20 concepts: named requirements and requires-clauses.
#include <concepts>
#include <iostream>
#include <string>

template <typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

template <Numeric T>
T twice(T value) { return value + value; }

template <typename T>
requires requires(T a, T b) { a + b; }
auto add(T a, T b) { return a + b; }

int main() {
    std::cout << twice(21) << ' ' << twice(1.5) << ' '
              << add(std::string("a"), std::string("b")) << '\n';
    return 0;
}
