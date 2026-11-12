/**
 * @file cache_locality.cpp
 * @brief Memory hierarchy alignment and cacheline optimizations for Rabin-Karp Rolling Hash Substring Matcher.
 * Module: rabin_karp_search
 */

#define RABIN_KARP_SEARCH_CACHELINE_SIZE 64
#define RABIN_KARP_SEARCH_BLOCK_SIZE 32

void rabin_karp_search_cache_blocked_operation(const double* in_mat, double* out_mat, size_t n) {
    for (size_t bi = 0; bi < n; bi += RABIN_KARP_SEARCH_BLOCK_SIZE) {
        size_t bi_end = (bi + RABIN_KARP_SEARCH_BLOCK_SIZE < n) ? (bi + RABIN_KARP_SEARCH_BLOCK_SIZE) : n;
        for (size_t bj = 0; bj < n; bj += RABIN_KARP_SEARCH_BLOCK_SIZE) {
            size_t bj_end = (bj + RABIN_KARP_SEARCH_BLOCK_SIZE < n) ? (bj + RABIN_KARP_SEARCH_BLOCK_SIZE) : n;
            for (size_t i = bi; i < bi_end; ++i) {
                for (size_t j = bj; j < bj_end; ++j) {
                    out_mat[i * n + j] = in_mat[i * n + j] * 1.000001;
                }
            }
        }
    }
}
