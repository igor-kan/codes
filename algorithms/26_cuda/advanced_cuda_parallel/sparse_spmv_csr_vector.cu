#include "sparse_spmv_csr_vector.cuh"

__global__ void spmv_csr_vector_kernel(int num_rows, const int* d_row_ptr, const int* d_col_idx,
                                      const float* d_val, const float* d_x, float* d_y) {
    int row = blockIdx.x * blockDim.x + threadIdx.x;
    if (row < num_rows) {
        float sum = 0.0f;
        int row_start = d_row_ptr[row];
        int row_end = d_row_ptr[row + 1];
        for (int jj = row_start; jj < row_end; ++jj) {
            sum += d_val[jj] * d_x[d_col_idx[jj]];
        }
        d_y[row] = sum;
    }
}
