/**
 * Conjugate Gradient in C (Numerical Recipes 3rd Ed. Chapter 2.7)
 */

#include <stdio.h>
#include <math.h>
#include <assert.h>

double dot(int n, const double* a, const double* b) {
    double s = 0;
    for (int i = 0; i < n; i++) s += a[i] * b[i];
    return s;
}

void conjugateGradient(double A[2][2], const double* b, double* x) {
    double r[2] = {b[0], b[1]};
    double p[2] = {r[0], r[1]};
    double rsOld = dot(2, r, r);

    for (int iter = 0; iter < 20; iter++) {
        if (sqrt(rsOld) < 1e-8) break;
        double Ap[2] = {
            A[0][0] * p[0] + A[0][1] * p[1],
            A[1][0] * p[0] + A[1][1] * p[1]
        };
        double alpha = rsOld / dot(2, p, Ap);
        x[0] += alpha * p[0];
        x[1] += alpha * p[1];
        r[0] -= alpha * Ap[0];
        r[1] -= alpha * Ap[1];
        double rsNew = dot(2, r, r);
        p[0] = r[0] + (rsNew / rsOld) * p[0];
        p[1] = r[1] + (rsNew / rsOld) * p[1];
        rsOld = rsNew;
    }
}

int main(void) {
    double A[2][2] = {{4, 1}, {1, 3}};
    double b[2] = {1, 2};
    double x[2] = {0};
    conjugateGradient(A, b, x);
    assert(fabs(x[0] - 1.0 / 11.0) < 1e-5);
    printf("C Conjugate Gradient verified.\n");
    return 0;
}
