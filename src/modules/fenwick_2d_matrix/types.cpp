/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for 2D Binary Indexed Tree (Fenwick Matrix) Range Updater.
 * Module: fenwick_2d_matrix | Algorithm Family: fenwick_2d
 */

#ifndef FENWICK_2D_MATRIX_TYPES_H
#define FENWICK_2D_MATRIX_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define FENWICK_2D_MATRIX_ALIGNMENT 64
#define FENWICK_2D_MATRIX_CAPACITY 4096

typedef struct fenwick_2d_matrix_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} fenwick_2d_matrix_config_t;

typedef struct fenwick_2d_matrix_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    double accumulator;
    fenwick_2d_matrix_config_t config;
} fenwick_2d_matrix_state_t;

#endif /* FENWICK_2D_MATRIX_TYPES_H */
