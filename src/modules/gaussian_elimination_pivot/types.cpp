/**
 * @file types.cpp
 * @brief Core types and configuration for Gaussian Elimination with Scaled Partial Pivoting.
 * Module: gaussian_elimination_pivot
 */

#ifndef GAUSSIAN_ELIMINATION_PIVOT_TYPES_H
#define GAUSSIAN_ELIMINATION_PIVOT_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define GAUSSIAN_ELIMINATION_PIVOT_ALIGNMENT 64
#define GAUSSIAN_ELIMINATION_PIVOT_DEFAULT_SZ 8192

typedef struct gaussian_elimination_pivot_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} gaussian_elimination_pivot_config_t;

typedef struct gaussian_elimination_pivot_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    gaussian_elimination_pivot_config_t config;
} gaussian_elimination_pivot_state_t;

#endif /* GAUSSIAN_ELIMINATION_PIVOT_TYPES_H */
