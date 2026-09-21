#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "brent_root_finding.h"

static double f_cubic(double x) {
    return x * x * x - 2.0 * x - 5.0; // Root at x approx 2.0945514815
}

int main(void) {
    double root = brent_find_root(f_cubic, 2.0, 3.0, 1e-8, 100);
    assert(fabs(f_cubic(root)) < 1e-7);
    printf("test_brent_root_finding PASSED\n");
    return 0;
}
