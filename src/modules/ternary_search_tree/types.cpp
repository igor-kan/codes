/**
 * @file types.cpp
 * @brief Core types and configuration for Ternary Search Trie Compact String Dictionary.
 * Module: ternary_search_tree
 */

#ifndef TERNARY_SEARCH_TREE_TYPES_H
#define TERNARY_SEARCH_TREE_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define TERNARY_SEARCH_TREE_ALIGNMENT 64
#define TERNARY_SEARCH_TREE_CAPACITY 2048

typedef struct ternary_search_tree_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} ternary_search_tree_config_t;

typedef struct ternary_search_tree_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    ternary_search_tree_config_t config;
} ternary_search_tree_state_t;

#endif /* TERNARY_SEARCH_TREE_TYPES_H */
