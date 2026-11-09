/**
 * @file types.cpp
 * @brief Core types and configuration for Chan Optimal 2D Convex Hull Geometric Engine.
 * Module: convex_hull_chan
 */

#ifndef CONVEX_HULL_CHAN_TYPES_H
#define CONVEX_HULL_CHAN_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define CONVEX_HULL_CHAN_ALIGNMENT 64
#define CONVEX_HULL_CHAN_CAPACITY 2048

typedef struct convex_hull_chan_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} convex_hull_chan_config_t;

typedef struct convex_hull_chan_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    convex_hull_chan_config_t config;
} convex_hull_chan_state_t;

#endif /* CONVEX_HULL_CHAN_TYPES_H */
