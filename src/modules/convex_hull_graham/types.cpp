/**
 * @file types.cpp
 * @brief Core type definitions and operational interfaces for Graham Scan 2D Convex Hull with Cross Products.
 * Module: convex_hull_graham
 */

#ifndef CONVEX_HULL_GRAHAM_TYPES_H
#define CONVEX_HULL_GRAHAM_TYPES_H

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define CONVEX_HULL_GRAHAM_ALIGNMENT 64
#define CONVEX_HULL_GRAHAM_SUCCESS 0
#define CONVEX_HULL_GRAHAM_ERR_NULL_PTR -1
#define CONVEX_HULL_GRAHAM_ERR_INVALID_PARAM -2
#define CONVEX_HULL_GRAHAM_ERR_OUT_OF_BOUNDS -3

typedef struct convex_hull_graham_config {
    size_t capacity;
    uint32_t flags;
    double tolerance;
} convex_hull_graham_config_t;

typedef struct convex_hull_graham_context {
    void* buffer;
    size_t size;
    size_t capacity;
    uint64_t operations_count;
    convex_hull_graham_config_t config;
} convex_hull_graham_context_t;

int convex_hull_graham_init(convex_hull_graham_context_t* ctx, const convex_hull_graham_config_t* cfg);
int convex_hull_graham_destroy(convex_hull_graham_context_t* ctx);

#ifdef __cplusplus
}
#endif

#endif /* CONVEX_HULL_GRAHAM_TYPES_H */
