/* LU decomposition with partial pivoting (Numerical Recipes 2.3). */
#include <assert.h>
#include <math.h>
#include <stdio.h>

static void lu_solve(double a[3][3], double *b, double *x) {
    int n = 3;
    for (int col = 0; col < n; ++col) {
        int pivot = col;
        for (int r = col + 1; r < n; ++r)
            if (fabs(a[r][col]) > fabs(a[pivot][col])) pivot = r;
        for (int k = 0; k < n; ++k) {
            double t = a[col][k]; a[col][k] = a[pivot][k]; a[pivot][k] = t;
        }
        double tb = b[col]; b[col] = b[pivot]; b[pivot] = tb;
        for (int r = col + 1; r < n; ++r) {
            double f = a[r][col] / a[col][col];
            for (int k = col; k < n; ++k) a[r][k] -= f * a[col][k];
            b[r] -= f * b[col];
        }
    }
    for (int r = n - 1; r >= 0; --r) {
        double s = b[r];
        for (int k = r + 1; k < n; ++k) s -= a[r][k] * x[k];
        x[r] = s / a[r][r];
    }
}

int main(void) {
    double a[3][3] = {{2, 1, -1}, {-3, -1, 2}, {-2, 1, 2}};
    double b[3] = {8, -11, -3}, x[3];
    lu_solve(a, b, x);
    assert(fabs(x[0] - 2) < 1e-9 && fabs(x[1] - 3) < 1e-9 && fabs(x[2] + 1) < 1e-9);
    printf("lu decomposition ok\n");
    return 0;
}
