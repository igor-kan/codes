/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Graham Scan 2D Convex Hull Vectorized Geometry.
 * Module: graham_scan_2d | Algorithm Family: geometry
 */

#ifndef GRAHAM_SCAN_2D_TYPES_H
#define GRAHAM_SCAN_2D_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define GRAHAM_SCAN_2D_ALIGNMENT 64
#define GRAHAM_SCAN_2D_BASE_CAPACITY 1024

typedef struct graham_scan_2d_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} graham_scan_2d_config_t;

typedef struct graham_scan_2d_state {
    void* buffer;
    size_t count;
    uint64_t operations;
    double accumulator;
    graham_scan_2d_config_t config;
} graham_scan_2d_state_t;

#endif /* GRAHAM_SCAN_2D_TYPES_H */
