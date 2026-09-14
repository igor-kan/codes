// Effective C++ -- auto and decltype deduction rules.
#include <iostream>
#include <type_traits>
#include <vector>

int main() {
    auto i = 42;                 // int
    auto d = 3.14;               // double
    const auto &ref = i;         // const int&
    auto copy = ref;             // int (reference dropped)
    decltype(i) j = i;           // int

    static_assert(std::is_same_v<decltype(i), int>);
    static_assert(std::is_same_v<decltype(ref), const int &>);

    std::vector<bool> flags{true, false};
    auto bit = flags[0];         // std::vector<bool>::reference proxy
    std::cout << i << ' ' << d << ' ' << copy << ' ' << std::boolalpha << bit << '\n';
    return 0;
}
