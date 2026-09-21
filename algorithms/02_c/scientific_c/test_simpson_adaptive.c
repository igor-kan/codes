#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "simpson_adaptive.h"

static double f_sine(double x) {
    return sin(x);
}

int main(void) {
    // int_0^pi sin(x) dx = 2.0
    double val = adaptive_simpson(f_sine, 0.0, 3.141592653589793, 1e-8);
    assert(fabs(val - 2.0) < 1e-6);
    printf("test_simpson_adaptive PASSED\n");
    return 0;
}
