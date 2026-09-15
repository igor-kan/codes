#include <assert.h>
#include <math.h>
#include <stdio.h>

static double f(double t, double y) { (void)t; return y; }

static double heun_method(double (*func)(double, double), double y, double t, double t1, int steps) {
    double h = (t1 - t) / steps;
    for (int i = 0; i < steps; ++i) {
        double k1 = func(t, y);
        double k2 = func(t + h, y + h * k1);
        y += 0.5 * h * (k1 + k2);
        t += h;
    }
    return y;
}

int main(void) {
    double value = heun_method(f, 1.0, 0.0, 1.0, 1000);
    assert(fabs(value - M_E) < 1e-4);
    printf("heun method ok\n");
    return 0;
}
