/**
 * @file types.cpp
 * @brief Core types and configuration for Schonhage-Strassen Fast Integer & Polynomial Multiply.
 * Module: matrix_schassen
 */

#ifndef MATRIX_SCHASSEN_TYPES_H
#define MATRIX_SCHASSEN_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define MATRIX_SCHASSEN_ALIGNMENT 64
#define MATRIX_SCHASSEN_CAPACITY 4096

typedef struct matrix_schassen_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} matrix_schassen_config_t;

typedef struct matrix_schassen_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    matrix_schassen_config_t config;
} matrix_schassen_state_t;

#endif /* MATRIX_SCHASSEN_TYPES_H */
