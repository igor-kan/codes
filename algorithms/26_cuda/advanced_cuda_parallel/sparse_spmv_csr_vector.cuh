#ifndef SPARSE_SPMV_CSR_VECTOR_CUH
#define SPARSE_SPMV_CSR_VECTOR_CUH

__global__ void spmv_csr_vector_kernel(int num_rows, const int* d_row_ptr, const int* d_col_idx,
                                      const float* d_val, const float* d_x, float* d_y);

#endif
