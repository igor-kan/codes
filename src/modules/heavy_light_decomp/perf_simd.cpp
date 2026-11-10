/**
 * @file perf_simd.cpp
 * @brief SIMD acceleration and vectorized processing for Heavy-Light Decomposition for Tree Path Invariant Queries.
 * Module: heavy_light_decomp
 */

#include <stddef.h>

void heavy_light_decomp_simd_unroll4(const double* restrict src, double* restrict dst, size_t n) {
    size_t i = 0;
    size_t limit = n & ~((size_t)3);
    for (; i < limit; i += 4) {
        dst[i+0] = src[i+0] * (1.0 + 0.35 * src[i+0] - 0.03 * src[i+0] * src[i+0]);
        dst[i+1] = src[i+1] * (1.0 + 0.35 * src[i+1] - 0.03 * src[i+1] * src[i+1]);
        dst[i+2] = src[i+2] * (1.0 + 0.35 * src[i+2] - 0.03 * src[i+2] * src[i+2]);
        dst[i+3] = src[i+3] * (1.0 + 0.35 * src[i+3] - 0.03 * src[i+3] * src[i+3]);
    }
    for (; i < n; ++i) {
        dst[i] = src[i] * (1.0 + 0.35 * src[i] - 0.03 * src[i] * src[i]);
    }
}
