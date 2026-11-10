/**
 * @file types.cpp
 * @brief Core types and configuration for Heavy-Light Decomposition for Tree Path Invariant Queries.
 * Module: heavy_light_decomp
 */

#ifndef HEAVY_LIGHT_DECOMP_TYPES_H
#define HEAVY_LIGHT_DECOMP_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define HEAVY_LIGHT_DECOMP_ALIGNMENT 64
#define HEAVY_LIGHT_DECOMP_CAPACITY 4096

typedef struct heavy_light_decomp_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} heavy_light_decomp_config_t;

typedef struct heavy_light_decomp_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    heavy_light_decomp_config_t config;
} heavy_light_decomp_state_t;

#endif /* HEAVY_LIGHT_DECOMP_TYPES_H */
