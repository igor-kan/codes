/**
 * @file types.cpp
 * @brief Core types and configuration for Continuous Domain Simulated Annealing Global Optimizer.
 * Module: simulated_annealing
 */

#ifndef SIMULATED_ANNEALING_TYPES_H
#define SIMULATED_ANNEALING_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define SIMULATED_ANNEALING_ALIGNMENT 64
#define SIMULATED_ANNEALING_DEFAULT_SZ 8192

typedef struct simulated_annealing_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} simulated_annealing_config_t;

typedef struct simulated_annealing_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    simulated_annealing_config_t config;
} simulated_annealing_state_t;

#endif /* SIMULATED_ANNEALING_TYPES_H */
