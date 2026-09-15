#include <assert.h>
#include <math.h>
#include <stdio.h>

static double g(double x) { return 0.5 * (x + 2.0 / x); }

static double fixed_point(double (*func)(double), double x) {
    for (int i = 0; i < 200; ++i) {
        double next = func(x);
        if (fabs(next - x) < 1e-12) return next;
        x = next;
    }
    return x;
}

int main(void) {
    assert(fabs(fixed_point(g, 1.0) - sqrt(2.0)) < 1e-9);
    printf("fixed point ok\n");
    return 0;
}
