/**
 * nCr mod p using precomputed factorials and modular inverse.
 */

#include <vector>
#include <cassert>
#include <iostream>

class Comb {
    long long MOD;
    std::vector<long long> fact, invfact;

    long long powmod(long long b, long long e) const {
        long long r = 1;
        b %= MOD;
        while (e) {
            if (e & 1) r = r * b % MOD;
            b = b * b % MOD;
            e >>= 1;
        }
        return r;
    }

public:
    Comb(int maxN, long long mod) : MOD(mod), fact(maxN + 1), invfact(maxN + 1) {
        fact[0] = 1;
        for (int i = 1; i <= maxN; ++i) fact[i] = fact[i - 1] * i % MOD;
        invfact[maxN] = powmod(fact[maxN], MOD - 2);
        for (int i = maxN; i >= 1; --i) invfact[i - 1] = invfact[i] * i % MOD;
    }

    long long nCr(int n, int r) const {
        if (r < 0 || r > n) return 0;
        return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD;
    }
};

int main() {
    const long long MOD = 1000000007;
    Comb comb(100, MOD);
    assert(comb.nCr(5, 2) == 10);
    assert(comb.nCr(10, 3) == 120);
    assert(comb.nCr(10, 0) == 1);
    assert(comb.nCr(10, 10) == 1);
    assert(comb.nCr(5, 6) == 0);
    std::cout << "[C++ NCR] Combinations modulo prime verified." << std::endl;
    return 0;
}
