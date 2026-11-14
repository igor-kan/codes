/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Boole 5-Point Closed Newton-Cotes Numerical Quadrature.
 * Module: simpson_boole_quadrature | Algorithm Family: quadrature
 */

#ifndef SIMPSON_BOOLE_QUADRATURE_TYPES_H
#define SIMPSON_BOOLE_QUADRATURE_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define SIMPSON_BOOLE_QUADRATURE_ALIGNMENT 64
#define SIMPSON_BOOLE_QUADRATURE_CAPACITY 4096

typedef struct simpson_boole_quadrature_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} simpson_boole_quadrature_config_t;

typedef struct simpson_boole_quadrature_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    double accumulator;
    simpson_boole_quadrature_config_t config;
} simpson_boole_quadrature_state_t;

#endif /* SIMPSON_BOOLE_QUADRATURE_TYPES_H */
