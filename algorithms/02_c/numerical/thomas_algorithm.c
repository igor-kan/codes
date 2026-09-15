#include <assert.h>
#include <math.h>
#include <stdio.h>

static void thomas(const double *lower, const double *diagonal, const double *upper,
                   const double *rhs, int n, double *x) {
    double c[16], d[16];
    c[0] = upper[0] / diagonal[0];
    d[0] = rhs[0] / diagonal[0];
    for (int i = 1; i < n; ++i) {
        double denominator = diagonal[i] - lower[i] * c[i - 1];
        c[i] = (i < n - 1) ? upper[i] / denominator : 0.0;
        d[i] = (rhs[i] - lower[i] * d[i - 1]) / denominator;
    }
    x[n - 1] = d[n - 1];
    for (int i = n - 2; i >= 0; --i) x[i] = d[i] - c[i] * x[i + 1];
}

int main(void) {
    double lower[3] = {0, -1, -1}, diagonal[3] = {2, 2, 2};
    double upper[3] = {-1, -1, 0}, rhs[3] = {1, 0, 1}, x[3];
    thomas(lower, diagonal, upper, rhs, 3, x);
    for (int i = 0; i < 3; ++i) assert(fabs(x[i] - 1.0) < 1e-12);
    printf("thomas algorithm ok\n");
    return 0;
}
