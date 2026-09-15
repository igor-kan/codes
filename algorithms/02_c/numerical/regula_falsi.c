#include <assert.h>
#include <math.h>
#include <stdio.h>

static double f(double x) { return x * x - 2.0; }

static double regula_falsi(double (*func)(double), double a, double b) {
    double fa = func(a), fb = func(b);
    double c = a;
    for (int i = 0; i < 200; ++i) {
        c = (a * fb - b * fa) / (fb - fa);
        double fc = func(c);
        if (fabs(fc) < 1e-12) return c;
        if (fa * fc < 0) { b = c; fb = fc; } else { a = c; fa = fc; }
    }
    return c;
}

int main(void) {
    assert(fabs(regula_falsi(f, 0.0, 2.0) - sqrt(2.0)) < 1e-9);
    printf("regula falsi ok\n");
    return 0;
}
