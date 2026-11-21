#include "interface.hpp"
#include <chrono>
#include <iostream>

int main() {
    using namespace codes_manacher_palindrome_radii;
    std::string b_s = "amanaplanacanalpanama";
    auto t0 = std::chrono::steady_clock::now();
    volatile std::int64_t sink = 0;
    for (int iter = 0; iter < 500; ++iter) {
        sink += static_cast<long long>(manacher_longest_palindrome(b_s).size());
    }
    auto t1 = std::chrono::steady_clock::now();
    auto us = std::chrono::duration_cast<std::chrono::microseconds>(t1 - t0).count();
    std::cout << "manacher_palindrome_radii us=" << us << " sink=" << sink << "\n";
    return 0;
}
