#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
long long gcd(long long a, long long b) {
    while (b) { long long t = b; b = a % b; a = t; }
    return a;
}
long long pollardRho(long long n) {
    if (n % 2 == 0) return 2;
    long long x = 2, y = 2, d = 1, c = 1;
    while (d == 1) {
        x = ((x * x) % n + c) % n;
        y = ((y * y) % n + c) % n;
        y = ((y * y) % n + c) % n;
        d = gcd(labs(x - y), n);
    }
    return d;
}
int main(void) {
    long long f = pollardRho(8051);
    assert(f == 83 || f == 97);
    printf("C Pollard Rho verified.\n");
    return 0;
}
