#include "fast_fourier_transform.h"
#include <math.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

void fft_cooley_tukey(double complex *x, int n) {
    if (n <= 1) return;
    
    // Bit reversal permutation
    int j = 0;
    for (int i = 0; i < n - 1; ++i) {
        if (i < j) {
            double complex temp = x[i];
            x[i] = x[j];
            x[j] = temp;
        }
        int k = n / 2;
        while (k <= j) {
            j -= k;
            k /= 2;
        }
        j += k;
    }
    
    // Cooley-Tukey butterfly
    for (int len = 2; len <= n; len <<= 1) {
        double angle = -2.0 * M_PI / len;
        double complex wlen = cos(angle) + I * sin(angle);
        for (int i = 0; i < n; i += len) {
            double complex w = 1.0 + 0.0 * I;
            for (int k = 0; k < len / 2; ++k) {
                double complex u = x[i + k];
                double complex v = x[i + k + len / 2] * w;
                x[i + k] = u + v;
                x[i + k + len / 2] = u - v;
                w *= wlen;
            }
        }
    }
}
