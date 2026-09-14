#include <stdio.h>

static long long egcd(long long a, long long b, long long *x, long long *y) {
    if (b == 0) { *x = 1; *y = 0; return a; }
    long long x1, y1;
    long long g = egcd(b, a % b, &x1, &y1);
    *x = y1;
    *y = x1 - (a / b) * y1;
    return g;
}

static long long mod_inv(long long a, long long m) {
    long long x, y;
    egcd(a, m, &x, &y);
    x %= m;
    if (x < 0) x += m;
    return x;
}

long long crt(const long long *r, const long long *m, int k) {
    long long M = 1, x = 0;
    for (int i = 0; i < k; ++i) M *= m[i];
    for (int i = 0; i < k; ++i) {
        long long Mi = M / m[i];
        long long inv = mod_inv(Mi, m[i]);
        x += r[i] * Mi * inv;
        x %= M;
    }
    return (x + M) % M;
}

int main(void) {
    long long r[] = {2, 3, 2};
    long long m[] = {3, 5, 7};

    long long x = crt(r, m, 3);
    if (x != 23) {
        printf("[C CRT] FAILED: x = %lld, want 23\n", x);
        return 1;
    }
    printf("[C CRT] x = 23 solves x%%3=2, x%%5=3, x%%7=2 verified\n");
    return 0;
}
