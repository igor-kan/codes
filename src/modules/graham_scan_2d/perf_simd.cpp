/**
 * @file perf_simd.cpp
 * @brief Multi-lane vectorization and loop unrolling for Graham Scan 2D Convex Hull Vectorized Geometry.
 * Module: graham_scan_2d
 */

#include <stddef.h>

void graham_scan_2d_vector_loop_unroll4(const double* restrict src, double* restrict dst, size_t n, double factor) {
    size_t i = 0;
    size_t unroll_limit = n & ~((size_t)3);
    for (; i < unroll_limit; i += 4) {
        dst[i+0] = src[i+0] * factor;
        dst[i+1] = src[i+1] * factor;
        dst[i+2] = src[i+2] * factor;
        dst[i+3] = src[i+3] * factor;
    }
    for (; i < n; ++i) {
        dst[i] = src[i] * factor;
    }
}
