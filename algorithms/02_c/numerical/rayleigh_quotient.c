#include <assert.h>
#include <math.h>
#include <stdio.h>

static double rayleigh(double matrix[2][2], const double *vector, double *eigenvector) {
    double scale = fmax(fabs(vector[0]), fabs(vector[1]));
    double x[2] = {vector[0] / scale, vector[1] / scale};
    double eigenvalue = 0.0;
    for (int iteration = 0; iteration < 100; ++iteration) {
        double p0 = matrix[0][0] * x[0] + matrix[0][1] * x[1];
        double p1 = matrix[1][0] * x[0] + matrix[1][1] * x[1];
        double norm = fmax(fabs(p0), fabs(p1));
        x[0] = p0 / norm;
        x[1] = p1 / norm;
        double numerator = x[0] * (matrix[0][0] * x[0] + matrix[0][1] * x[1])
                         + x[1] * (matrix[1][0] * x[0] + matrix[1][1] * x[1]);
        double denominator = x[0] * x[0] + x[1] * x[1];
        double next = numerator / denominator;
        if (fabs(next - eigenvalue) < 1e-12) { eigenvalue = next; break; }
        eigenvalue = next;
    }
    if (eigenvector) { eigenvector[0] = x[0]; eigenvector[1] = x[1]; }
    return eigenvalue;
}

int main(void) {
    double matrix[2][2] = {{2, 1}, {1, 2}}, vector[2] = {1, 0}, eigenvector[2];
    assert(fabs(rayleigh(matrix, vector, eigenvector) - 3.0) < 1e-9);
    printf("rayleigh quotient ok\n");
    return 0;
}
