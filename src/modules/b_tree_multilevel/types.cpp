/**
 * @file types.cpp
 * @brief Core types and configuration for Multi-Level Balanced B-Tree with Node Split-Merge.
 * Module: b_tree_multilevel
 */

#ifndef B_TREE_MULTILEVEL_TYPES_H
#define B_TREE_MULTILEVEL_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define B_TREE_MULTILEVEL_ALIGNMENT 64
#define B_TREE_MULTILEVEL_DEFAULT_SZ 8192

typedef struct b_tree_multilevel_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} b_tree_multilevel_config_t;

typedef struct b_tree_multilevel_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    b_tree_multilevel_config_t config;
} b_tree_multilevel_state_t;

#endif /* B_TREE_MULTILEVEL_TYPES_H */
