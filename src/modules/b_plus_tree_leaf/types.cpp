/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Leaf-Chained B+ Tree Index Structure for Range Scans.
 * Module: b_plus_tree_leaf | Algorithm Family: b_plus_tree
 */

#ifndef B_PLUS_TREE_LEAF_TYPES_H
#define B_PLUS_TREE_LEAF_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define B_PLUS_TREE_LEAF_ALIGNMENT 64
#define B_PLUS_TREE_LEAF_CAPACITY 4096

typedef struct b_plus_tree_leaf_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} b_plus_tree_leaf_config_t;

typedef struct b_plus_tree_leaf_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    double accumulator;
    b_plus_tree_leaf_config_t config;
} b_plus_tree_leaf_state_t;

#endif /* B_PLUS_TREE_LEAF_TYPES_H */
