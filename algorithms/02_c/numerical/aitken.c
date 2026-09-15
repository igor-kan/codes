#include <assert.h>
#include <math.h>
#include <stdio.h>

static double aitken(double x0, double x1, double x2) {
    double denominator = x2 - 2.0 * x1 + x0;
    if (fabs(denominator) < 1e-15) return x2;
    return x2 - (x2 - x1) * (x2 - x1) / denominator;
}

int main(void) {
    assert(fabs(aitken(1.0, 0.5, 0.25)) < 1e-12);
    double sequence[3];
    for (int n = 0; n < 3; ++n) sequence[n] = 2.0 - 2.0 * pow(0.5, n);
    assert(fabs(aitken(sequence[0], sequence[1], sequence[2]) - 2.0) < 1e-12);
    printf("aitken ok\n");
    return 0;
}
