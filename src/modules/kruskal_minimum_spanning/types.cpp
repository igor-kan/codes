/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Kruskal Minimum Spanning Tree with Disjoint Set Union.
 * Module: kruskal_minimum_spanning | Algorithm Family: graph_algo
 */

#ifndef KRUSKAL_MINIMUM_SPANNING_TYPES_H
#define KRUSKAL_MINIMUM_SPANNING_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define KRUSKAL_MINIMUM_SPANNING_ALIGNMENT 64
#define KRUSKAL_MINIMUM_SPANNING_CAPACITY 2048

typedef struct kruskal_minimum_spanning_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} kruskal_minimum_spanning_config_t;

typedef struct kruskal_minimum_spanning_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    double accumulator;
    kruskal_minimum_spanning_config_t config;
} kruskal_minimum_spanning_state_t;

#endif /* KRUSKAL_MINIMUM_SPANNING_TYPES_H */
