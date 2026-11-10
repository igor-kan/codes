/**
 * @file types.cpp
 * @brief Core types and configuration for Goldberg-Tarjan Push-Relabel Maximum Flow Network.
 * Module: push_relabel_maxflow
 */

#ifndef PUSH_RELABEL_MAXFLOW_TYPES_H
#define PUSH_RELABEL_MAXFLOW_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define PUSH_RELABEL_MAXFLOW_ALIGNMENT 64
#define PUSH_RELABEL_MAXFLOW_CAPACITY 4096

typedef struct push_relabel_maxflow_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} push_relabel_maxflow_config_t;

typedef struct push_relabel_maxflow_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    push_relabel_maxflow_config_t config;
} push_relabel_maxflow_state_t;

#endif /* PUSH_RELABEL_MAXFLOW_TYPES_H */
