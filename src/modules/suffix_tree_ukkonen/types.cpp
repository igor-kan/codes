/**
 * @file types.cpp
 * @brief Core types and configuration for Ukkonen Linear-Time Online Suffix Tree Construction.
 * Module: suffix_tree_ukkonen
 */

#ifndef SUFFIX_TREE_UKKONEN_TYPES_H
#define SUFFIX_TREE_UKKONEN_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define SUFFIX_TREE_UKKONEN_ALIGNMENT 64
#define SUFFIX_TREE_UKKONEN_CAPACITY 4096

typedef struct suffix_tree_ukkonen_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} suffix_tree_ukkonen_config_t;

typedef struct suffix_tree_ukkonen_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    suffix_tree_ukkonen_config_t config;
} suffix_tree_ukkonen_state_t;

#endif /* SUFFIX_TREE_UKKONEN_TYPES_H */
