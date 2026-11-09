/**
 * @file types.cpp
 * @brief Core types and configuration for Segment Tree with Lazy Propagation Range Updates.
 * Module: segment_tree_lazy
 */

#ifndef SEGMENT_TREE_LAZY_TYPES_H
#define SEGMENT_TREE_LAZY_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define SEGMENT_TREE_LAZY_ALIGNMENT 64
#define SEGMENT_TREE_LAZY_CAPACITY 2048

typedef struct segment_tree_lazy_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} segment_tree_lazy_config_t;

typedef struct segment_tree_lazy_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    segment_tree_lazy_config_t config;
} segment_tree_lazy_state_t;

#endif /* SEGMENT_TREE_LAZY_TYPES_H */
