/**
 * @file types.cpp
 * @brief Core type definitions and operational interfaces for Augmented Red-Black Interval Stabbing Tree.
 * Module: interval_tree
 */

#ifndef INTERVAL_TREE_TYPES_H
#define INTERVAL_TREE_TYPES_H

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define INTERVAL_TREE_ALIGNMENT 64
#define INTERVAL_TREE_SUCCESS 0
#define INTERVAL_TREE_ERR_NULL_PTR -1
#define INTERVAL_TREE_ERR_INVALID_PARAM -2
#define INTERVAL_TREE_ERR_OUT_OF_BOUNDS -3

typedef struct interval_tree_config {
    size_t capacity;
    uint32_t flags;
    double tolerance;
} interval_tree_config_t;

typedef struct interval_tree_context {
    void* buffer;
    size_t size;
    size_t capacity;
    uint64_t operations_count;
    interval_tree_config_t config;
} interval_tree_context_t;

int interval_tree_init(interval_tree_context_t* ctx, const interval_tree_config_t* cfg);
int interval_tree_destroy(interval_tree_context_t* ctx);

#ifdef __cplusplus
}
#endif

#endif /* INTERVAL_TREE_TYPES_H */
