/**
 * Modular inverse via extended Euclid and Fermat's little theorem.
 */

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

// Works for any coprime a, m.
long long modInverseEuclid(long long a, long long m) {
    long long x, y;
    long long g = extgcd(a, m, x, y);
    if (g != 1) return -1; // inverse does not exist
    x %= m;
    if (x < 0) x += m;
    return x;
}

long long powmod(long long b, long long e, long long m) {
    long long r = 1;
    b %= m;
    while (e) {
        if (e & 1) r = r * b % m;
        b = b * b % m;
        e >>= 1;
    }
    return r;
}

// Requires p to be prime.
long long modInverseFermat(long long a, long long p) {
    return powmod(a, p - 2, p);
}

int main() {
    const long long MOD = 1000000007;
    assert(modInverseEuclid(3, 11) == 4);
    assert(modInverseEuclid(10, 17) == 12);
    assert(modInverseFermat(3, MOD) == modInverseEuclid(3, MOD));
    assert(modInverseFermat(123456, MOD) == modInverseEuclid(123456, MOD));
    assert(3 * modInverseFermat(3, MOD) % MOD == 1);
    std::cout << "[C++ ModInverse] Extended Euclid and Fermat inverses verified." << std::endl;
    return 0;
}
