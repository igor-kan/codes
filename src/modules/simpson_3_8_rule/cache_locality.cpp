/**
 * @file cache_locality.cpp
 * @brief Memory hierarchy alignment and cacheline optimizations for Composite Simpson 3/8 Rule Numerical Integrator.
 * Module: simpson_3_8_rule
 */

#define SIMPSON_3_8_RULE_CACHELINE_SIZE 64
#define SIMPSON_3_8_RULE_BLOCK_SIZE 32

void simpson_3_8_rule_cache_blocked_operation(const double* in_mat, double* out_mat, size_t n) {
    for (size_t bi = 0; bi < n; bi += SIMPSON_3_8_RULE_BLOCK_SIZE) {
        size_t bi_end = (bi + SIMPSON_3_8_RULE_BLOCK_SIZE < n) ? (bi + SIMPSON_3_8_RULE_BLOCK_SIZE) : n;
        for (size_t bj = 0; bj < n; bj += SIMPSON_3_8_RULE_BLOCK_SIZE) {
            size_t bj_end = (bj + SIMPSON_3_8_RULE_BLOCK_SIZE < n) ? (bj + SIMPSON_3_8_RULE_BLOCK_SIZE) : n;
            for (size_t i = bi; i < bi_end; ++i) {
                for (size_t j = bj; j < bj_end; ++j) {
                    out_mat[i * n + j] = in_mat[i * n + j] * 1.000001;
                }
            }
        }
    }
}
