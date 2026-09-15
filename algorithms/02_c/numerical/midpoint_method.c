#include <assert.h>
#include <math.h>
#include <stdio.h>

static double f(double t, double y) { (void)t; return y; }

static double midpoint_method(double (*func)(double, double), double y, double t, double t1, int steps) {
    double h = (t1 - t) / steps;
    for (int i = 0; i < steps; ++i) {
        double k1 = func(t, y);
        double k2 = func(t + h / 2, y + h * k1 / 2);
        y += h * k2;
        t += h;
    }
    return y;
}

int main(void) {
    double value = midpoint_method(f, 1.0, 0.0, 1.0, 1000);
    assert(fabs(value - M_E) < 1e-4);
    printf("midpoint method ok\n");
    return 0;
}
