/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Dijkstra 3-Way Partitioning Quicksort for Duplicates.
 * Module: quicksort_three_way | Algorithm Family: sorting
 */

#ifndef QUICKSORT_THREE_WAY_TYPES_H
#define QUICKSORT_THREE_WAY_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define QUICKSORT_THREE_WAY_ALIGNMENT 64
#define QUICKSORT_THREE_WAY_CAPACITY 4096

typedef struct quicksort_three_way_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} quicksort_three_way_config_t;

typedef struct quicksort_three_way_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    double accumulator;
    quicksort_three_way_config_t config;
} quicksort_three_way_state_t;

#endif /* QUICKSORT_THREE_WAY_TYPES_H */
