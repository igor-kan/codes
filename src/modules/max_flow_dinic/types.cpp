/**
 * @file types.cpp
 * @brief Core types and configuration for Dinic Maximum Flow Network with Level Graphs.
 * Module: max_flow_dinic
 */

#ifndef MAX_FLOW_DINIC_TYPES_H
#define MAX_FLOW_DINIC_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define MAX_FLOW_DINIC_ALIGNMENT 64
#define MAX_FLOW_DINIC_CAPACITY 2048

typedef struct max_flow_dinic_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} max_flow_dinic_config_t;

typedef struct max_flow_dinic_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    max_flow_dinic_config_t config;
} max_flow_dinic_state_t;

#endif /* MAX_FLOW_DINIC_TYPES_H */
