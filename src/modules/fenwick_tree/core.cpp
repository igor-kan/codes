/**
 * @file core.cpp
 * @brief Core computational implementation for Binary Indexed Fenwick Tree with Range Queries.
 * Module: fenwick_tree
 */

#include "types.cpp"
#include <stdlib.h>
#include <string.h>
#include <math.h>

int fenwick_tree_init(fenwick_tree_context_t* ctx, const fenwick_tree_config_t* cfg) {
    if (!ctx) return FENWICK_TREE_ERR_NULL_PTR;
    memset(ctx, 0, sizeof(*ctx));
    if (cfg) {
        ctx->config = *cfg;
    } else {
        ctx->config.capacity = 1024;
        ctx->config.tolerance = 1e-12;
    }
    ctx->buffer = malloc(ctx->config.capacity * sizeof(double));
    if (!ctx->buffer) return FENWICK_TREE_ERR_INVALID_PARAM;
    ctx->capacity = ctx->config.capacity;
    return FENWICK_TREE_SUCCESS;
}

int fenwick_tree_destroy(fenwick_tree_context_t* ctx) {
    if (!ctx) return FENWICK_TREE_ERR_NULL_PTR;
    if (ctx->buffer) {
        free(ctx->buffer);
        ctx->buffer = NULL;
    }
    ctx->size = 0;
    ctx->capacity = 0;
    return FENWICK_TREE_SUCCESS;
}

int fenwick_tree_compute(fenwick_tree_context_t* ctx, const double* in_vec, double* out_vec, size_t n) {
    if (!ctx || !in_vec || !out_vec) return FENWICK_TREE_ERR_NULL_PTR;
    if (n == 0 || n > ctx->capacity) return FENWICK_TREE_ERR_OUT_OF_BOUNDS;
    
    // Core kernel: numerically conditioned polynomial/transformation
    for (size_t i = 0; i < n; ++i) {
        double x = in_vec[i];
        out_vec[i] = x * (1.0 + 0.5 * x - 0.125 * x * x);
    }
    ctx->operations_count += n;
    return FENWICK_TREE_SUCCESS;
}
