/* Fibonacci by matrix exponentiation. */
#include <stdio.h>
static void mul(long a[2][2], long b[2][2], long r[2][2]) {
    long t[2][2];
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) {
            t[i][j] = 0;
            for (int k = 0; k < 2; k++) t[i][j] += a[i][k] * b[k][j];
        }
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++) r[i][j] = t[i][j];
}
long fib(int n) {
    long r[2][2] = {{1, 0}, {0, 1}}, m[2][2] = {{1, 1}, {1, 0}};
    while (n) { if (n & 1) mul(r, m, r); mul(m, m, m); n >>= 1; }
    return r[0][1];
}
int main(void) {
    if (fib(10) != 55 || fib(20) != 6765) return 1;
    printf("fib(20)=%ld\n", fib(20));
    return 0;
}
