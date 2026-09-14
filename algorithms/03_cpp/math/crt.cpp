/**
 * Chinese Remainder Theorem: solve x = r_i (mod m_i) for pairwise coprime moduli.
 */

#include <vector>
#include <cassert>
#include <iostream>

long long extgcd(long long a, long long b, long long& x, long long& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long g = extgcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

long long modInverse(long long a, long long m) {
    long long x, y;
    extgcd(a, m, x, y);
    x %= m;
    if (x < 0) x += m;
    return x;
}

// Pairwise coprime moduli. Returns x mod (product of moduli).
long long crt(const std::vector<long long>& rem, const std::vector<long long>& mod) {
    long long x = 0;
    long long M = 1;
    for (size_t i = 0; i < mod.size(); ++i) {
        long long m = mod[i];
        long long r = ((rem[i] % m) + m) % m;
        // Solve M * t == r - x (mod m). gcd(M, m) == 1 since moduli are pairwise coprime.
        long long a = M % m;
        long long b = ((r - x) % m + m) % m;
        long long t = b * modInverse(a, m) % m;
        x += M * t;
        M *= m;
        x %= M;
        if (x < 0) x += M;
    }
    return x;
}

int main() {
    auto x = crt({2, 3, 2}, {3, 5, 7});
    assert(x == 23); // 23 % 3 == 2, 23 % 5 == 3, 23 % 7 == 2
    auto y = crt({1, 2, 3}, {2, 3, 5});
    assert(y == 23);
    std::cout << "[C++ CRT] Chinese Remainder Theorem verified." << std::endl;
    return 0;
}
