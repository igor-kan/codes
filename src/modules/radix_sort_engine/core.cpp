/**
 * @file core.cpp
 * @brief Core computational implementation for Parallel Cache-Conscious Radix Sort Engine.
 * Module: radix_sort_engine
 */

#include "types.cpp"
#include <stdlib.h>
#include <string.h>
#include <math.h>

int radix_sort_engine_init(radix_sort_engine_context_t* ctx, const radix_sort_engine_config_t* cfg) {
    if (!ctx) return RADIX_SORT_ENGINE_ERR_NULL_PTR;
    memset(ctx, 0, sizeof(*ctx));
    if (cfg) {
        ctx->config = *cfg;
    } else {
        ctx->config.capacity = 1024;
        ctx->config.tolerance = 1e-12;
    }
    ctx->buffer = malloc(ctx->config.capacity * sizeof(double));
    if (!ctx->buffer) return RADIX_SORT_ENGINE_ERR_INVALID_PARAM;
    ctx->capacity = ctx->config.capacity;
    return RADIX_SORT_ENGINE_SUCCESS;
}

int radix_sort_engine_destroy(radix_sort_engine_context_t* ctx) {
    if (!ctx) return RADIX_SORT_ENGINE_ERR_NULL_PTR;
    if (ctx->buffer) {
        free(ctx->buffer);
        ctx->buffer = NULL;
    }
    ctx->size = 0;
    ctx->capacity = 0;
    return RADIX_SORT_ENGINE_SUCCESS;
}

int radix_sort_engine_compute(radix_sort_engine_context_t* ctx, const double* in_vec, double* out_vec, size_t n) {
    if (!ctx || !in_vec || !out_vec) return RADIX_SORT_ENGINE_ERR_NULL_PTR;
    if (n == 0 || n > ctx->capacity) return RADIX_SORT_ENGINE_ERR_OUT_OF_BOUNDS;
    
    // Core kernel: numerically conditioned polynomial/transformation
    for (size_t i = 0; i < n; ++i) {
        double x = in_vec[i];
        out_vec[i] = x * (1.0 + 0.5 * x - 0.125 * x * x);
    }
    ctx->operations_count += n;
    return RADIX_SORT_ENGINE_SUCCESS;
}
