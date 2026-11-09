/**
 * @file types.cpp
 * @brief Core types and configuration for Hopcroft-Tarjan Articulation Points and Bridges.
 * Module: biconnected_components
 */

#ifndef BICONNECTED_COMPONENTS_TYPES_H
#define BICONNECTED_COMPONENTS_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define BICONNECTED_COMPONENTS_ALIGNMENT 64
#define BICONNECTED_COMPONENTS_CAPACITY 2048

typedef struct biconnected_components_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} biconnected_components_config_t;

typedef struct biconnected_components_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    biconnected_components_config_t config;
} biconnected_components_state_t;

#endif /* BICONNECTED_COMPONENTS_TYPES_H */
