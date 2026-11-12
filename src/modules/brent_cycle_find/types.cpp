/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Brent Teleporting Tortoise and Hare Cycle Detector.
 * Module: brent_cycle_find | Algorithm Family: cycle_find
 */

#ifndef BRENT_CYCLE_FIND_TYPES_H
#define BRENT_CYCLE_FIND_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define BRENT_CYCLE_FIND_ALIGNMENT 64
#define BRENT_CYCLE_FIND_BASE_CAPACITY 1024

typedef struct brent_cycle_find_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} brent_cycle_find_config_t;

typedef struct brent_cycle_find_state {
    void* buffer;
    size_t count;
    uint64_t operations;
    double accumulator;
    brent_cycle_find_config_t config;
} brent_cycle_find_state_t;

#endif /* BRENT_CYCLE_FIND_TYPES_H */
