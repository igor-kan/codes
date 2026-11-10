/**
 * @file types.cpp
 * @brief Core types and configuration for R*-Tree Spatial Index with Topological Reinsertion.
 * Module: spatial_rtree_star
 */

#ifndef SPATIAL_RTREE_STAR_TYPES_H
#define SPATIAL_RTREE_STAR_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define SPATIAL_RTREE_STAR_ALIGNMENT 64
#define SPATIAL_RTREE_STAR_CAPACITY 4096

typedef struct spatial_rtree_star_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} spatial_rtree_star_config_t;

typedef struct spatial_rtree_star_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    spatial_rtree_star_config_t config;
} spatial_rtree_star_state_t;

#endif /* SPATIAL_RTREE_STAR_TYPES_H */
