#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "matrix_inversion_lu.h"

int main(void) {
    double A[3][3] = {
        {1.0, 2.0, 3.0},
        {0.0, 1.0, 4.0},
        {5.0, 6.0, 0.0}
    };
    double invA[3][3];
    int ok = invert_matrix_3x3(A, invA);
    assert(ok == 1);
    
    // Check A * invA = I
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            double sum = 0.0;
            for (int k = 0; k < 3; ++k) sum += A[i][k] * invA[k][j];
            double expected = (i == j) ? 1.0 : 0.0;
            assert(fabs(sum - expected) < 1e-6);
        }
    }
    printf("test_matrix_inversion_lu PASSED\n");
    return 0;
}
