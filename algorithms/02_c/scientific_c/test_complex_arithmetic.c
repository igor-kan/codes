#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "complex_arithmetic.h"

int main(void) {
    // Euler's identity: exp(i * pi) = -1
    Cplx ipi = {0.0, M_PI};
    Cplx res = cplx_exp(ipi);
    assert(fabs(res.real - (-1.0)) < 1e-6);
    assert(fabs(res.imag - 0.0) < 1e-6);
    printf("test_complex_arithmetic PASSED\n");
    return 0;
}
