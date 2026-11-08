/**
 * @file types.cpp
 * @brief Core type definitions and operational interfaces for Binary Indexed Fenwick Tree with Range Queries.
 * Module: fenwick_tree
 */

#ifndef FENWICK_TREE_TYPES_H
#define FENWICK_TREE_TYPES_H

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define FENWICK_TREE_ALIGNMENT 64
#define FENWICK_TREE_SUCCESS 0
#define FENWICK_TREE_ERR_NULL_PTR -1
#define FENWICK_TREE_ERR_INVALID_PARAM -2
#define FENWICK_TREE_ERR_OUT_OF_BOUNDS -3

typedef struct fenwick_tree_config {
    size_t capacity;
    uint32_t flags;
    double tolerance;
} fenwick_tree_config_t;

typedef struct fenwick_tree_context {
    void* buffer;
    size_t size;
    size_t capacity;
    uint64_t operations_count;
    fenwick_tree_config_t config;
} fenwick_tree_context_t;

int fenwick_tree_init(fenwick_tree_context_t* ctx, const fenwick_tree_config_t* cfg);
int fenwick_tree_destroy(fenwick_tree_context_t* ctx);

#ifdef __cplusplus
}
#endif

#endif /* FENWICK_TREE_TYPES_H */
