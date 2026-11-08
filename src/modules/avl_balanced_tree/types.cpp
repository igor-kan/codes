/**
 * @file types.cpp
 * @brief Core types and configuration for Self-Balancing AVL Search Tree with Rotations.
 * Module: avl_balanced_tree
 */

#ifndef AVL_BALANCED_TREE_TYPES_H
#define AVL_BALANCED_TREE_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define AVL_BALANCED_TREE_ALIGNMENT 64
#define AVL_BALANCED_TREE_DEFAULT_CAPACITY 1024

typedef struct avl_balanced_tree_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} avl_balanced_tree_config_t;

typedef struct avl_balanced_tree_state {
    void* memory_arena;
    size_t count;
    uint64_t metric_cycles;
    avl_balanced_tree_config_t config;
} avl_balanced_tree_state_t;

#endif /* AVL_BALANCED_TREE_TYPES_H */
