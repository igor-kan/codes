#include <stdio.h>

long long euler_totient(long long n) {
    long long result = n;
    for (long long p = 2; p * p <= n; ++p) {
        if (n % p == 0) {
            while (n % p == 0) n /= p;
            result -= result / p;
        }
    }
    if (n > 1) result -= result / n;
    return result;
}

int main(void) {
    if (euler_totient(1) != 1 || euler_totient(12) != 4 || euler_totient(100) != 40 || euler_totient(7) != 6) {
        printf("[C EulerTotient] FAILED: phi mismatch\n");
        return 1;
    }
    printf("[C EulerTotient] phi(1)=1 phi(12)=4 phi(100)=40 phi(7)=6 verified\n");
    return 0;
}
