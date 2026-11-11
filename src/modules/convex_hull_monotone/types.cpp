/**
 * @file types.cpp
 * @brief Core types and configuration for Monotone Chain (Andrew Algorithm) 2D Convex Hull.
 * Module: convex_hull_monotone
 */

#ifndef CONVEX_HULL_MONOTONE_TYPES_H
#define CONVEX_HULL_MONOTONE_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define CONVEX_HULL_MONOTONE_ALIGNMENT 64
#define CONVEX_HULL_MONOTONE_DEFAULT_SZ 8192

typedef struct convex_hull_monotone_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} convex_hull_monotone_config_t;

typedef struct convex_hull_monotone_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    convex_hull_monotone_config_t config;
} convex_hull_monotone_state_t;

#endif /* CONVEX_HULL_MONOTONE_TYPES_H */
