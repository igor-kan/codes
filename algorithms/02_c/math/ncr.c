#include <stdio.h>

#define MOD 1000000007LL
#define MAXN 1000000

static long long fact[MAXN + 1];
static long long inv_fact[MAXN + 1];

static long long mod_pow(long long base, long long exp, long long m) {
    long long res = 1;
    base %= m;
    while (exp > 0) {
        if (exp & 1) res = res * base % m;
        base = base * base % m;
        exp >>= 1;
    }
    return res;
}

void ncr_init(int n) {
    fact[0] = 1;
    for (int i = 1; i <= n; ++i) fact[i] = fact[i - 1] * i % MOD;
    inv_fact[n] = mod_pow(fact[n], MOD - 2, MOD);
    for (int i = n - 1; i >= 0; --i) inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD;
}

long long ncr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD;
}

int main(void) {
    ncr_init(100);

    if (ncr(5, 2) != 10 || ncr(10, 3) != 120 || ncr(10, 0) != 1 || ncr(4, 5) != 0) {
        printf("[C NCR] FAILED: binomial coefficient mismatch\n");
        return 1;
    }
    printf("[C NCR] nCr mod p via factorials verified\n");
    return 0;
}
