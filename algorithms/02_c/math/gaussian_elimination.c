/* Gaussian elimination with partial pivoting. */
#include <stdio.h>
#include <math.h>
int main(void) {
    double a[3][4] = {{2, 1, -1, 8}, {-3, -1, 2, -11}, {-2, 1, 2, -3}};
    for (int c = 0; c < 3; c++) {
        int p = c;
        for (int r = c + 1; r < 3; r++) if (fabs(a[r][c]) > fabs(a[p][c])) p = r;
        for (int k = 0; k < 4; k++) { double t = a[c][k]; a[c][k] = a[p][k]; a[p][k] = t; }
        for (int r = c + 1; r < 3; r++) {
            double f = a[r][c] / a[c][c];
            for (int k = c; k < 4; k++) a[r][k] -= f * a[c][k];
        }
    }
    double x[3];
    for (int r = 2; r >= 0; r--) {
        double s = a[r][3];
        for (int k = r + 1; k < 3; k++) s -= a[r][k] * x[k];
        x[r] = s / a[r][r];
    }
    if (fabs(x[0] - 2) > 1e-9 || fabs(x[1] - 3) > 1e-9 || fabs(x[2] + 1) > 1e-9) return 1;
    printf("x=%g %g %g\n", x[0], x[1], x[2]);
    return 0;
}
