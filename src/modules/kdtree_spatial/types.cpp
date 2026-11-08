/**
 * @file types.cpp
 * @brief Core types and configuration for Multi-Dimensional K-d Tree Nearest Neighbor Engine.
 * Module: kdtree_spatial
 */

#ifndef KDTREE_SPATIAL_TYPES_H
#define KDTREE_SPATIAL_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define KDTREE_SPATIAL_ALIGNMENT 64
#define KDTREE_SPATIAL_DEFAULT_CAPACITY 1024

typedef struct kdtree_spatial_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} kdtree_spatial_config_t;

typedef struct kdtree_spatial_state {
    void* memory_arena;
    size_t count;
    uint64_t metric_cycles;
    kdtree_spatial_config_t config;
} kdtree_spatial_state_t;

#endif /* KDTREE_SPATIAL_TYPES_H */
