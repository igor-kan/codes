/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Wagner-Fischer Dynamic Programming Edit Distance.
 * Module: levenshtein_distance | Algorithm Family: dp_matrix
 */

#ifndef LEVENSHTEIN_DISTANCE_TYPES_H
#define LEVENSHTEIN_DISTANCE_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define LEVENSHTEIN_DISTANCE_ALIGNMENT 64
#define LEVENSHTEIN_DISTANCE_BASE_CAPACITY 1024

typedef struct levenshtein_distance_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} levenshtein_distance_config_t;

typedef struct levenshtein_distance_state {
    void* buffer;
    size_t count;
    uint64_t operations;
    double accumulator;
    levenshtein_distance_config_t config;
} levenshtein_distance_state_t;

#endif /* LEVENSHTEIN_DISTANCE_TYPES_H */
