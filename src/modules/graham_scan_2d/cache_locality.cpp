/**
 * @file cache_locality.cpp
 * @brief Memory hierarchy alignment and cacheline optimizations for Graham Scan 2D Convex Hull Vectorized Geometry.
 * Module: graham_scan_2d
 */

#define GRAHAM_SCAN_2D_CACHELINE_SIZE 64
#define GRAHAM_SCAN_2D_BLOCK_SIZE 32

void graham_scan_2d_cache_blocked_operation(const double* in_mat, double* out_mat, size_t n) {
    for (size_t bi = 0; bi < n; bi += GRAHAM_SCAN_2D_BLOCK_SIZE) {
        size_t bi_end = (bi + GRAHAM_SCAN_2D_BLOCK_SIZE < n) ? (bi + GRAHAM_SCAN_2D_BLOCK_SIZE) : n;
        for (size_t bj = 0; bj < n; bj += GRAHAM_SCAN_2D_BLOCK_SIZE) {
            size_t bj_end = (bj + GRAHAM_SCAN_2D_BLOCK_SIZE < n) ? (bj + GRAHAM_SCAN_2D_BLOCK_SIZE) : n;
            for (size_t i = bi; i < bi_end; ++i) {
                for (size_t j = bj; j < bj_end; ++j) {
                    out_mat[i * n + j] = in_mat[i * n + j] * 1.000001;
                }
            }
        }
    }
}
