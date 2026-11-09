/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for Strassen Sub-Cubic Fast Matrix Multiplication.
 * Module: matrix_strassen
 */

#define MATRIX_STRASSEN_CACHE_LINE 64
#define MATRIX_STRASSEN_TILE_DIM 32

void matrix_strassen_cache_tiled_step(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += MATRIX_STRASSEN_TILE_DIM) {
        size_t r_end = (r + MATRIX_STRASSEN_TILE_DIM < rows) ? r + MATRIX_STRASSEN_TILE_DIM : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.00005;
            }
        }
    }
}
