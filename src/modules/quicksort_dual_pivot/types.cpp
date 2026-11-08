/**
 * @file types.cpp
 * @brief Core types and configuration for Yaroslavskiy Dual-Pivot Vectorized Quicksort.
 * Module: quicksort_dual_pivot
 */

#ifndef QUICKSORT_DUAL_PIVOT_TYPES_H
#define QUICKSORT_DUAL_PIVOT_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define QUICKSORT_DUAL_PIVOT_ALIGNMENT 64
#define QUICKSORT_DUAL_PIVOT_DEFAULT_CAPACITY 1024

typedef struct quicksort_dual_pivot_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} quicksort_dual_pivot_config_t;

typedef struct quicksort_dual_pivot_state {
    void* memory_arena;
    size_t count;
    uint64_t metric_cycles;
    quicksort_dual_pivot_config_t config;
} quicksort_dual_pivot_state_t;

#endif /* QUICKSORT_DUAL_PIVOT_TYPES_H */
