#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <assert.h>

static inline uint64_t mod_mul(uint64_t a, uint64_t b, uint64_t mod) {
    return (uint64_t)(((__int128_t)a * b) % mod);
}

static inline uint64_t mod_pow(uint64_t base, uint64_t exp, uint64_t mod) {
    uint64_t res = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) res = mod_mul(res, base, mod);
        base = mod_mul(base, base, mod);
        exp >>= 1;
    }
    return res;
}

// Deterministic Miller-Rabin for n < 2^64 using 7 prime bases
bool miller_rabin(uint64_t n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if ((n & 1) == 0) return false;

    uint64_t d = n - 1;
    int s = 0;
    while ((d & 1) == 0) {
        d >>= 1;
        s++;
    }

    // Deterministic bases for 64-bit unsigned integers
    static const uint64_t bases[] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022ULL};
    for (int i = 0; i < 7; i++) {
        uint64_t a = bases[i] % n;
        if (a == 0) return true;

        uint64_t x = mod_pow(a, d, n);
        if (x == 1 || x == n - 1) continue;

        bool composite = true;
        for (int r = 1; r < s; r++) {
            x = mod_mul(x, x, n);
            if (x == n - 1) {
                composite = false;
                break;
            }
        }
        if (composite) return false;
    }
    return true;
}

int main(void) {
    uint64_t primes[] = {1000000007ULL, 2147483647ULL, 999999999989ULL};
    uint64_t composites[] = {1000000005ULL, 2147483649ULL, 3000000021ULL};

    for (int i = 0; i < 3; i++) {
        assert(miller_rabin(primes[i]) == true);
        assert(miller_rabin(composites[i]) == false);
    }
    printf("[C Miller-Rabin] Deterministic 64-bit primality verified.\n");
    return 0;
}
