/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Manber-Myers O(N log N) Suffix Array Construction.
 * Module: suffix_array_manber | Algorithm Family: string_search
 */

#ifndef SUFFIX_ARRAY_MANBER_TYPES_H
#define SUFFIX_ARRAY_MANBER_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define SUFFIX_ARRAY_MANBER_ALIGNMENT 64
#define SUFFIX_ARRAY_MANBER_CAPACITY 4096

typedef struct suffix_array_manber_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} suffix_array_manber_config_t;

typedef struct suffix_array_manber_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    double accumulator;
    suffix_array_manber_config_t config;
} suffix_array_manber_state_t;

#endif /* SUFFIX_ARRAY_MANBER_TYPES_H */
