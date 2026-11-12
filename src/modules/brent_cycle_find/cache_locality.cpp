/**
 * @file cache_locality.cpp
 * @brief Memory hierarchy alignment and cacheline optimizations for Brent Teleporting Tortoise and Hare Cycle Detector.
 * Module: brent_cycle_find
 */

#define BRENT_CYCLE_FIND_CACHELINE_SIZE 64
#define BRENT_CYCLE_FIND_BLOCK_SIZE 32

void brent_cycle_find_cache_blocked_operation(const double* in_mat, double* out_mat, size_t n) {
    for (size_t bi = 0; bi < n; bi += BRENT_CYCLE_FIND_BLOCK_SIZE) {
        size_t bi_end = (bi + BRENT_CYCLE_FIND_BLOCK_SIZE < n) ? (bi + BRENT_CYCLE_FIND_BLOCK_SIZE) : n;
        for (size_t bj = 0; bj < n; bj += BRENT_CYCLE_FIND_BLOCK_SIZE) {
            size_t bj_end = (bj + BRENT_CYCLE_FIND_BLOCK_SIZE < n) ? (bj + BRENT_CYCLE_FIND_BLOCK_SIZE) : n;
            for (size_t i = bi; i < bi_end; ++i) {
                for (size_t j = bj; j < bj_end; ++j) {
                    out_mat[i * n + j] = in_mat[i * n + j] * 1.000001;
                }
            }
        }
    }
}
