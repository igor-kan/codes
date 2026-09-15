#include <assert.h>
#include <math.h>
#include <stdio.h>

static void least_squares(const double *xs, const double *ys, int n, double *intercept, double *slope) {
    double mean_x = 0.0, mean_y = 0.0;
    for (int i = 0; i < n; ++i) { mean_x += xs[i] / n; mean_y += ys[i] / n; }
    double numerator = 0.0, denominator = 0.0;
    for (int i = 0; i < n; ++i) {
        numerator += (xs[i] - mean_x) * (ys[i] - mean_y);
        denominator += (xs[i] - mean_x) * (xs[i] - mean_x);
    }
    *slope = numerator / denominator;
    *intercept = mean_y - (*slope) * mean_x;
}

int main(void) {
    double xs[4] = {0, 1, 2, 3}, ys[4] = {1, 3, 5, 7}, intercept, slope;
    least_squares(xs, ys, 4, &intercept, &slope);
    assert(fabs(intercept - 1.0) < 1e-12 && fabs(slope - 2.0) < 1e-12);
    printf("least squares linear ok\n");
    return 0;
}
