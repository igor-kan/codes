/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Composite Simpson 3/8 Rule Numerical Integrator.
 * Module: simpson_3_8_rule | Algorithm Family: numerical_quad
 */

#ifndef SIMPSON_3_8_RULE_TYPES_H
#define SIMPSON_3_8_RULE_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define SIMPSON_3_8_RULE_ALIGNMENT 64
#define SIMPSON_3_8_RULE_BASE_CAPACITY 1024

typedef struct simpson_3_8_rule_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} simpson_3_8_rule_config_t;

typedef struct simpson_3_8_rule_state {
    void* buffer;
    size_t count;
    uint64_t operations;
    double accumulator;
    simpson_3_8_rule_config_t config;
} simpson_3_8_rule_state_t;

#endif /* SIMPSON_3_8_RULE_TYPES_H */
