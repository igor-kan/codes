/**
 * @file cache_locality.cpp
 * @brief Cache tiling and memory hierarchy optimizations for Gaussian Elimination with Scaled Partial Pivoting.
 * Module: gaussian_elimination_pivot
 */

#define GAUSSIAN_ELIMINATION_PIVOT_CACHE_LINE 64
#define GAUSSIAN_ELIMINATION_PIVOT_TILE_DIM 32

void gaussian_elimination_pivot_cache_tiled_step_v47(const double* in, double* out, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += GAUSSIAN_ELIMINATION_PIVOT_TILE_DIM) {
        size_t r_end = (r + GAUSSIAN_ELIMINATION_PIVOT_TILE_DIM < rows) ? r + GAUSSIAN_ELIMINATION_PIVOT_TILE_DIM : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_end; ++i) {
                out[i * cols + c] = in[i * cols + c] * 1.00002;
            }
        }
    }
}
