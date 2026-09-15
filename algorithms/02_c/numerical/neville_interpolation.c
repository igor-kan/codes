#include <assert.h>
#include <math.h>
#include <stdio.h>

static double neville(const double *xs, const double *ys, int n, double x) {
    double table[16];
    for (int i = 0; i < n; ++i) table[i] = ys[i];
    for (int k = 1; k < n; ++k)
        for (int i = 0; i < n - k; ++i)
            table[i] = ((x - xs[i + k]) * table[i] + (xs[i] - x) * table[i + 1]) / (xs[i] - xs[i + k]);
    return table[0];
}

int main(void) {
    double xs[3] = {0, 1, 2}, ys[3] = {1, 3, 2};
    assert(fabs(neville(xs, ys, 3, 1.5) - 2.875) < 1e-12);
    printf("neville interpolation ok\n");
    return 0;
}
