#include <assert.h>
#include <math.h>
#include <stdio.h>

static double square(double x) { return x * x; }

static double monte_carlo(double (*func)(double), double a, double b, int samples) {
    long long state = 42;
    const long long modulus = 1LL << 31;
    double total = 0.0;
    for (int i = 0; i < samples; ++i) {
        state = (1103515245LL * state + 12345) % modulus;
        total += func(a + (b - a) * (double)state / (double)modulus);
    }
    return (b - a) * total / samples;
}

int main(void) {
    assert(fabs(monte_carlo(square, 0.0, 1.0, 100000) - 1.0 / 3.0) < 0.01);
    printf("monte carlo integration ok\n");
    return 0;
}
