/**
 * Extended Euclidean Algorithm in C (CLRS 3rd Ed. Chapter 31.2)
 */

#include <stdio.h>
#include <assert.h>

long long extendedGCD(long long a, long long b, long long *x, long long *y) {
    if (b == 0) {
        *x = 1;
        *y = 0;
        return a;
    }
    long long x1, y1;
    long long gcd = extendedGCD(b, a % b, &x1, &y1);
    *x = y1;
    *y = x1 - (a / b) * y1;
    return gcd;
}

int main(void) {
    long long x, y;
    long long g = extendedGCD(240, 46, &x, &y);
    assert(g == 2);
    assert(240 * x + 46 * y == 2);
    printf("C Extended GCD verified.\n");
    return 0;
}
