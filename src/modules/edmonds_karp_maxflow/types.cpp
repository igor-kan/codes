/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Edmonds-Karp Maximum Bipartite Network Flow Engine.
 * Module: edmonds_karp_maxflow | Algorithm Family: network_flow
 */

#ifndef EDMONDS_KARP_MAXFLOW_TYPES_H
#define EDMONDS_KARP_MAXFLOW_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define EDMONDS_KARP_MAXFLOW_ALIGNMENT 64
#define EDMONDS_KARP_MAXFLOW_CAPACITY 4096

typedef struct edmonds_karp_maxflow_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} edmonds_karp_maxflow_config_t;

typedef struct edmonds_karp_maxflow_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    double accumulator;
    edmonds_karp_maxflow_config_t config;
} edmonds_karp_maxflow_state_t;

#endif /* EDMONDS_KARP_MAXFLOW_TYPES_H */
