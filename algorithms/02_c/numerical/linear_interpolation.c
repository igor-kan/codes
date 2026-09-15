#include <assert.h>
#include <math.h>
#include <stdio.h>

static double linear_interpolation(const double *xs, const double *ys, int n, double x) {
    if (x <= xs[0]) return ys[0];
    if (x >= xs[n - 1]) return ys[n - 1];
    for (int i = 1; i < n; ++i) {
        if (x <= xs[i]) {
            double slope = (ys[i] - ys[i - 1]) / (xs[i] - xs[i - 1]);
            return ys[i - 1] + slope * (x - xs[i - 1]);
        }
    }
    return ys[n - 1];
}

int main(void) {
    double xs[3] = {0, 1, 2}, ys[3] = {0, 2, 4};
    assert(fabs(linear_interpolation(xs, ys, 3, 0.5) - 1.0) < 1e-12);
    double xs2[3] = {0, 1, 4}, ys2[3] = {0, 1, 2};
    assert(fabs(linear_interpolation(xs2, ys2, 3, 2.5) - 1.5) < 1e-12);
    printf("linear interpolation ok\n");
    return 0;
}
