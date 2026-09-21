#ifndef MATRIX_TRANSPOSE_SHARED_MEM_CUH
#define MATRIX_TRANSPOSE_SHARED_MEM_CUH

#define TILE_DIM 32
#define BLOCK_ROWS 8

__global__ void transpose_no_bank_conflicts(float *odata, const float *idata, int width, int height);

#endif
