#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "polynomial_roots_laguerre.h"

int main(void) {
    // x^2 - 4 = 0 -> coeffs [-4, 0, 1]
    double coeffs[3] = {-4.0, 0.0, 1.0};
    double r = laguerre_root(coeffs, 2, 1.0, 1e-8, 50);
    assert(fabs(r - 2.0) < 1e-6);
    printf("test_polynomial_roots_laguerre PASSED\n");
    return 0;
}
