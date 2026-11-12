/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Rabin-Karp Rolling Hash Substring Matcher.
 * Module: rabin_karp_search | Algorithm Family: string_search
 */

#ifndef RABIN_KARP_SEARCH_TYPES_H
#define RABIN_KARP_SEARCH_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define RABIN_KARP_SEARCH_ALIGNMENT 64
#define RABIN_KARP_SEARCH_BASE_CAPACITY 1024

typedef struct rabin_karp_search_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} rabin_karp_search_config_t;

typedef struct rabin_karp_search_state {
    void* buffer;
    size_t count;
    uint64_t operations;
    double accumulator;
    rabin_karp_search_config_t config;
} rabin_karp_search_state_t;

#endif /* RABIN_KARP_SEARCH_TYPES_H */
