#ifndef SPARSE_MATRIX_CSR_H
#define SPARSE_MATRIX_CSR_H

typedef struct {
    int n_rows;
    int n_cols;
    int nnz;
    double *values;
    int *col_indices;
    int *row_ptr;
} CSRMatrix;

void csr_matvec(const CSRMatrix *A, const double *x, double *y);

#endif
