#include <stdio.h>

#define MOD 1000000007LL

static long long egcd(long long a, long long b, long long *x, long long *y) {
    if (b == 0) { *x = 1; *y = 0; return a; }
    long long x1, y1;
    long long g = egcd(b, a % b, &x1, &y1);
    *x = y1;
    *y = x1 - (a / b) * y1;
    return g;
}

long long mod_inv_extended(long long a, long long m) {
    long long x, y;
    long long g = egcd(a, m, &x, &y);
    if (g != 1) return -1;
    x %= m;
    if (x < 0) x += m;
    return x;
}

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

long long mod_inv_fermat(long long a, long long p) {
    return mod_pow(a, p - 2, p);
}

int main(void) {
    long long a = 3;
    long long inv_ext = mod_inv_extended(a, MOD);
    long long inv_fer = mod_inv_fermat(a, MOD);

    if (inv_ext != inv_fer || a * inv_ext % MOD != 1) {
        printf("[C ModInverse] FAILED: inverse mismatch\n");
        return 1;
    }
    if (mod_inv_extended(2, 4) != -1) {
        printf("[C ModInverse] FAILED: non-coprime should return -1\n");
        return 1;
    }
    printf("[C ModInverse] Extended Euclid + Fermat verified\n");
    return 0;
}
