/**
 * Cholesky LL^T in C (Numerical Recipes 3rd Ed. Chapter 2.6)
 */

#include <stdio.h>
#include <math.h>
#include <assert.h>

void cholesky(int n, double A[3][3], double L[3][3]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            double sum = 0;
            for (int k = 0; k < j; k++) sum += L[i][k] * L[j][k];
            if (i == j) {
                double val = A[i][i] - sum;
                assert(val > 0);
                L[i][j] = sqrt(val);
            } else {
                L[i][j] = (A[i][j] - sum) / L[j][j];
            }
        }
    }
}

int main(void) {
    double A[3][3] = {
        {4, 12, -16},
        {12, 37, -43},
        {-16, -43, 98}
    };
    double L[3][3] = {0};
    cholesky(3, A, L);
    assert(fabs(L[0][0] - 2.0) < 1e-6);
    printf("C Cholesky verified.\n");
    return 0;
}
