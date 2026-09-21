#include <stdio.h>
#include <math.h>
#include <assert.h>
#include "rk4_integrator.h"

static double exp_growth(double t, double y) {
    (void)t;
    return y; // dy/dt = y -> y(t) = exp(t)
}

int main(void) {
    double y = 1.0;
    double t = 0.0;
    double dt = 0.01;
    for (int i = 0; i < 100; ++i) {
        y = rk4_step(exp_growth, t, y, dt);
        t += dt;
    }
    // At t = 1.0, y approx e = 2.718281828...
    assert(fabs(y - exp(1.0)) < 1e-5);
    printf("test_rk4_integrator PASSED\n");
    return 0;
}
