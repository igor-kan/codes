// Variadic template max and compile-time recursion.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

template <typename T>
constexpr T maximum(T value) { return value; }

template <typename T, typename... Rest>
constexpr T maximum(T first, Rest... rest) {
    return std::max(first, maximum(rest...));
}

int main() {
    static_assert(maximum(1, 5, 3, 2) == 5);
    assert(maximum(std::string("a"), std::string("c"), std::string("b")) == "c");
    std::cout << maximum(1, 5, 3, 2) << '\n';
    return 0;
}
