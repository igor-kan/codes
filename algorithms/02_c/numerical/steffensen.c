#include <assert.h>
#include <math.h>
#include <stdio.h>

static double g(double x) { return 0.5 * (x + 2.0 / x); }

static double steffensen(double (*func)(double), double x) {
    for (int i = 0; i < 100; ++i) {
        double x1 = func(x), x2 = func(x1);
        double denominator = x2 - 2.0 * x1 + x;
        if (fabs(denominator) < 1e-15) return x2;
        double next = x - (x1 - x) * (x1 - x) / denominator;
        if (fabs(next - x) < 1e-12) return next;
        x = next;
    }
    return x;
}

int main(void) {
    assert(fabs(steffensen(g, 1.0) - sqrt(2.0)) < 1e-12);
    printf("steffensen ok\n");
    return 0;
}
