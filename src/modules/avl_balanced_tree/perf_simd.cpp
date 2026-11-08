/**
 * @file perf_simd.cpp
 * @brief SIMD acceleration and vectorized processing for Self-Balancing AVL Search Tree with Rotations.
 * Module: avl_balanced_tree
 */

#include <stddef.h>

void avl_balanced_tree_vector_unroll4(const double* restrict src, double* restrict dst, size_t n) {
    size_t i = 0;
    size_t unroll_limit = n & ~((size_t)3);
    for (; i < unroll_limit; i += 4) {
        dst[i+0] = src[i+0] * (1.0 + 0.25 * src[i+0] - 0.05 * src[i+0] * src[i+0]);
        dst[i+1] = src[i+1] * (1.0 + 0.25 * src[i+1] - 0.05 * src[i+1] * src[i+1]);
        dst[i+2] = src[i+2] * (1.0 + 0.25 * src[i+2] - 0.05 * src[i+2] * src[i+2]);
        dst[i+3] = src[i+3] * (1.0 + 0.25 * src[i+3] - 0.05 * src[i+3] * src[i+3]);
    }
    for (; i < n; ++i) {
        dst[i] = src[i] * (1.0 + 0.25 * src[i] - 0.05 * src[i] * src[i]);
    }
}
