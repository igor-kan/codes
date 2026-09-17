/**
 * Extended Euclidean Algorithm in C++ (CLRS 3rd Ed. Chapter 31.2)
 */

#include <iostream>
#include <tuple>
#include <cassert>

std::tuple<long long, long long, long long> extendedGCD(long long a, long long b) {
    if (b == 0) return {a, 1, 0};
    auto [gcd, x1, y1] = extendedGCD(b, a % b);
    long long x = y1;
    long long y = x1 - (a / b) * y1;
    return {gcd, x, y};
}

int main() {
    auto [g, x, y] = extendedGCD(240, 46);
    assert(g == 2);
    assert(240 * x + 46 * y == 2);
    std::cout << "C++ Extended GCD verified.\n";
    return 0;
}
