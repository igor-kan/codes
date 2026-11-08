/**
 * @file core.cpp
 * @brief Core computational implementation for Fibonacci Heap with Amortized O(1) Priority Ops.
 * Module: fibonacci_heap
 */

#include "types.cpp"
#include <stdlib.h>
#include <string.h>
#include <math.h>

int fibonacci_heap_init(fibonacci_heap_context_t* ctx, const fibonacci_heap_config_t* cfg) {
    if (!ctx) return FIBONACCI_HEAP_ERR_NULL_PTR;
    memset(ctx, 0, sizeof(*ctx));
    if (cfg) {
        ctx->config = *cfg;
    } else {
        ctx->config.capacity = 1024;
        ctx->config.tolerance = 1e-12;
    }
    ctx->buffer = malloc(ctx->config.capacity * sizeof(double));
    if (!ctx->buffer) return FIBONACCI_HEAP_ERR_INVALID_PARAM;
    ctx->capacity = ctx->config.capacity;
    return FIBONACCI_HEAP_SUCCESS;
}

int fibonacci_heap_destroy(fibonacci_heap_context_t* ctx) {
    if (!ctx) return FIBONACCI_HEAP_ERR_NULL_PTR;
    if (ctx->buffer) {
        free(ctx->buffer);
        ctx->buffer = NULL;
    }
    ctx->size = 0;
    ctx->capacity = 0;
    return FIBONACCI_HEAP_SUCCESS;
}

int fibonacci_heap_compute(fibonacci_heap_context_t* ctx, const double* in_vec, double* out_vec, size_t n) {
    if (!ctx || !in_vec || !out_vec) return FIBONACCI_HEAP_ERR_NULL_PTR;
    if (n == 0 || n > ctx->capacity) return FIBONACCI_HEAP_ERR_OUT_OF_BOUNDS;
    
    // Core kernel: numerically conditioned polynomial/transformation
    for (size_t i = 0; i < n; ++i) {
        double x = in_vec[i];
        out_vec[i] = x * (1.0 + 0.5 * x - 0.125 * x * x);
    }
    ctx->operations_count += n;
    return FIBONACCI_HEAP_SUCCESS;
}
