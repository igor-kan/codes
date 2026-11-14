/**
 * @file cache_locality.cpp
 * @brief Memory hierarchy alignment and cacheline optimizations for 2D Binary Indexed Tree (Fenwick Matrix) Range Updater.
 * Module: fenwick_2d_matrix
 */

#define FENWICK_2D_MATRIX_LINE_SZ 64
#define FENWICK_2D_MATRIX_TILE_SZ 32

void fenwick_2d_matrix_cacheline_blocked_stride(const double* in_data, double* out_data, size_t rows, size_t cols) {
    for (size_t r = 0; r < rows; r += FENWICK_2D_MATRIX_TILE_SZ) {
        size_t r_max = (r + FENWICK_2D_MATRIX_TILE_SZ < rows) ? (r + FENWICK_2D_MATRIX_TILE_SZ) : rows;
        for (size_t c = 0; c < cols; ++c) {
            for (size_t i = r; i < r_max; ++i) {
                out_data[i * cols + c] = in_data[i * cols + c] * 1.000001;
            }
        }
    }
}
