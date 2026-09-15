#include <assert.h>
#include <math.h>
#include <stdio.h>

static double f(double t, double y) { (void)t; return y; }

static double euler_method(double (*func)(double, double), double y, double t, double t1, int steps) {
    double h = (t1 - t) / steps;
    for (int i = 0; i < steps; ++i) {
        y += h * func(t, y);
        t += h;
    }
    return y;
}

int main(void) {
    double value = euler_method(f, 1.0, 0.0, 1.0, 1000);
    assert(fabs(value - M_E) < 0.01);
    printf("euler method ok\n");
    return 0;
}
