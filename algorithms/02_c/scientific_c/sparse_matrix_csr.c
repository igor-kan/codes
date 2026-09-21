#include "sparse_matrix_csr.h"

void csr_matvec(const CSRMatrix *A, const double *x, double *y) {
    for (int r = 0; r < A->n_rows; ++r) {
        double sum = 0.0;
        int start = A->row_ptr[r];
        int end = A->row_ptr[r + 1];
        for (int idx = start; idx < end; ++idx) {
            sum += A->values[idx] * x[A->col_indices[idx]];
        }
        y[r] = sum;
    }
}
