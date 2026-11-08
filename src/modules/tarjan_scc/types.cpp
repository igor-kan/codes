/**
 * @file types.cpp
 * @brief Core types and configuration for Tarjan Strongly Connected Components Low-Link Graph Engine.
 * Module: tarjan_scc
 */

#ifndef TARJAN_SCC_TYPES_H
#define TARJAN_SCC_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define TARJAN_SCC_ALIGNMENT 64
#define TARJAN_SCC_DEFAULT_CAPACITY 1024

typedef struct tarjan_scc_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} tarjan_scc_config_t;

typedef struct tarjan_scc_state {
    void* memory_arena;
    size_t count;
    uint64_t metric_cycles;
    tarjan_scc_config_t config;
} tarjan_scc_state_t;

#endif /* TARJAN_SCC_TYPES_H */
