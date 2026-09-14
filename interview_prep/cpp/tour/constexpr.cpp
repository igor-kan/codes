// A Tour of C++ -- constexpr and compile-time computation.
#include <array>
#include <iostream>

constexpr long factorial(int n) {
    long result = 1;
    for (int i = 2; i <= n; ++i) result *= i;
    return result;
}

constexpr std::array<long, 6> make_table() {
    std::array<long, 6> table{};
    for (int i = 0; i < 6; ++i) table[static_cast<std::size_t>(i)] = factorial(i);
    return table;
}

int main() {
    constexpr auto table = make_table();
    static_assert(factorial(5) == 120);
    std::cout << "5!=" << table[5] << '\n';
    return 0;
}
