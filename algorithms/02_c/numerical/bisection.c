#include <assert.h>
#include <math.h>
#include <stdio.h>

static double f(double x) { return x * x - 2.0; }

static double bisection(double (*func)(double), double a, double b) {
    double fa = func(a);
    for (int i = 0; i < 200; ++i) {
        double c = 0.5 * (a + b);
        double fc = func(c);
        if (fc == 0 || (b - a) / 2 < 1e-12) return c;
        if (fa * fc < 0) b = c; else { a = c; fa = fc; }
    }
    return 0.5 * (a + b);
}

int main(void) {
    assert(fabs(bisection(f, 0.0, 2.0) - sqrt(2.0)) < 1e-9);
    printf("bisection ok\n");
    return 0;
}
