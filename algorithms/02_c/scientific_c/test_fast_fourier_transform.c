#include <stdio.h>
#include <complex.h>
#include <math.h>
#include <assert.h>
#include "fast_fourier_transform.h"

int main(void) {
    int n = 8;
    double complex x[8];
    for (int i = 0; i < n; ++i) {
        x[i] = 1.0 + 0.0 * I; // DC pulse
    }
    fft_cooley_tukey(x, n);
    // DC component x[0] should be 8.0, all others 0
    assert(cabs(x[0] - 8.0) < 1e-6);
    for (int i = 1; i < n; ++i) {
        assert(cabs(x[i]) < 1e-6);
    }
    printf("test_fast_fourier_transform PASSED\n");
    return 0;
}
