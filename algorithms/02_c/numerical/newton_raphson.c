/* Newton-Raphson root finding (Numerical Recipes 9.4). */
#include <assert.h>
#include <math.h>
#include <stdio.h>

static double newton(double (*f)(double), double (*df)(double), double x) {
    for (int i = 0; i < 100; ++i) {
        double fx = f(x);
        if (fabs(fx) < 1e-12) break;
        x -= fx / df(x);
    }
    return x;
}

static double f(double x) { return x * x - 2; }
static double df(double x) { return 2 * x; }

int main(void) {
    double root = newton(f, df, 1.0);
    assert(fabs(root - sqrt(2.0)) < 1e-9);
    printf("newton-raphson ok\n");
    return 0;
}
