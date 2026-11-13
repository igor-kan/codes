/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Adaptive Simpson Numerical Quadrature Integrator.
 * Module: simpson_adaptive_quad | Algorithm Family: quadrature
 */

#ifndef SIMPSON_ADAPTIVE_QUAD_TYPES_H
#define SIMPSON_ADAPTIVE_QUAD_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define SIMPSON_ADAPTIVE_QUAD_ALIGNMENT 64
#define SIMPSON_ADAPTIVE_QUAD_CAPACITY 2048

typedef struct simpson_adaptive_quad_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} simpson_adaptive_quad_config_t;

typedef struct simpson_adaptive_quad_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    double accumulator;
    simpson_adaptive_quad_config_t config;
} simpson_adaptive_quad_state_t;

#endif /* SIMPSON_ADAPTIVE_QUAD_TYPES_H */
