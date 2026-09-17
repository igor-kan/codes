#include <numeric>
#include <cassert>
#include <iostream>
long long pollardRho(long long n) {
    if (n % 2 == 0) return 2;
    long long x = 2, y = 2, d = 1, c = 1;
    auto f = [n, c](long long val) { return ((val * val) % n + c) % n; };
    while (d == 1) {
        x = f(x);
        y = f(f(y));
        d = std::gcd(std::abs(x - y), n);
    }
    return d;
}
int main() {
    long long factor = pollardRho(8051);
    assert(factor == 83 || factor == 97);
    std::cout << "C++ Pollard's Rho verified.\n";
}
