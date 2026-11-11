/**
 * @file types.cpp
 * @brief Core types and configuration for Disjoint-Set Union (DSU) with Path Compression and Rank.
 * Module: disjoint_set_union
 */

#ifndef DISJOINT_SET_UNION_TYPES_H
#define DISJOINT_SET_UNION_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define DISJOINT_SET_UNION_ALIGNMENT 64
#define DISJOINT_SET_UNION_DEFAULT_SZ 8192

typedef struct disjoint_set_union_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} disjoint_set_union_config_t;

typedef struct disjoint_set_union_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    disjoint_set_union_config_t config;
} disjoint_set_union_state_t;

#endif /* DISJOINT_SET_UNION_TYPES_H */
