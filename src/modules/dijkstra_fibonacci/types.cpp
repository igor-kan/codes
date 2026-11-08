/**
 * @file types.cpp
 * @brief Core types and configuration for Dijkstra Shortest Path with Fibonacci Priority Queue.
 * Module: dijkstra_fibonacci
 */

#ifndef DIJKSTRA_FIBONACCI_TYPES_H
#define DIJKSTRA_FIBONACCI_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define DIJKSTRA_FIBONACCI_ALIGNMENT 64
#define DIJKSTRA_FIBONACCI_DEFAULT_CAPACITY 1024

typedef struct dijkstra_fibonacci_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} dijkstra_fibonacci_config_t;

typedef struct dijkstra_fibonacci_state {
    void* memory_arena;
    size_t count;
    uint64_t metric_cycles;
    dijkstra_fibonacci_config_t config;
} dijkstra_fibonacci_state_t;

#endif /* DIJKSTRA_FIBONACCI_TYPES_H */
