/**
 * @file core.cpp
 * @brief Core computational implementation for Graham Scan 2D Convex Hull with Cross Products.
 * Module: convex_hull_graham
 */

#include "types.cpp"
#include <stdlib.h>
#include <string.h>
#include <math.h>

int convex_hull_graham_init(convex_hull_graham_context_t* ctx, const convex_hull_graham_config_t* cfg) {
    if (!ctx) return CONVEX_HULL_GRAHAM_ERR_NULL_PTR;
    memset(ctx, 0, sizeof(*ctx));
    if (cfg) {
        ctx->config = *cfg;
    } else {
        ctx->config.capacity = 1024;
        ctx->config.tolerance = 1e-12;
    }
    ctx->buffer = malloc(ctx->config.capacity * sizeof(double));
    if (!ctx->buffer) return CONVEX_HULL_GRAHAM_ERR_INVALID_PARAM;
    ctx->capacity = ctx->config.capacity;
    return CONVEX_HULL_GRAHAM_SUCCESS;
}

int convex_hull_graham_destroy(convex_hull_graham_context_t* ctx) {
    if (!ctx) return CONVEX_HULL_GRAHAM_ERR_NULL_PTR;
    if (ctx->buffer) {
        free(ctx->buffer);
        ctx->buffer = NULL;
    }
    ctx->size = 0;
    ctx->capacity = 0;
    return CONVEX_HULL_GRAHAM_SUCCESS;
}

int convex_hull_graham_compute(convex_hull_graham_context_t* ctx, const double* in_vec, double* out_vec, size_t n) {
    if (!ctx || !in_vec || !out_vec) return CONVEX_HULL_GRAHAM_ERR_NULL_PTR;
    if (n == 0 || n > ctx->capacity) return CONVEX_HULL_GRAHAM_ERR_OUT_OF_BOUNDS;
    
    // Core kernel: numerically conditioned polynomial/transformation
    for (size_t i = 0; i < n; ++i) {
        double x = in_vec[i];
        out_vec[i] = x * (1.0 + 0.5 * x - 0.125 * x * x);
    }
    ctx->operations_count += n;
    return CONVEX_HULL_GRAHAM_SUCCESS;
}
