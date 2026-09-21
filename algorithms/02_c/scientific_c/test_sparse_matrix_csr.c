#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "sparse_matrix_csr.h"

int main(void) {
    double values[3] = {10.0, 20.0, 30.0};
    int col_indices[3] = {0, 1, 1};
    int row_ptr[3] = {0, 2, 3}; // 2 rows
    CSRMatrix A = {2, 2, 3, values, col_indices, row_ptr};
    
    double x[2] = {1.0, 2.0};
    double y[2];
    csr_matvec(&A, x, y);
    // y[0] = 10*1 + 20*2 = 50
    // y[1] = 30*2 = 60
    assert(fabs(y[0] - 50.0) < 1e-6);
    assert(fabs(y[1] - 60.0) < 1e-6);
    printf("test_sparse_matrix_csr PASSED\n");
    return 0;
}
