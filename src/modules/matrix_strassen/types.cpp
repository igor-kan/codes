/**
 * @file types.cpp
 * @brief Core types and configuration for Strassen Sub-Cubic Fast Matrix Multiplication.
 * Module: matrix_strassen
 */

#ifndef MATRIX_STRASSEN_TYPES_H
#define MATRIX_STRASSEN_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define MATRIX_STRASSEN_ALIGNMENT 64
#define MATRIX_STRASSEN_CAPACITY 2048

typedef struct matrix_strassen_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} matrix_strassen_config_t;

typedef struct matrix_strassen_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    matrix_strassen_config_t config;
} matrix_strassen_state_t;

#endif /* MATRIX_STRASSEN_TYPES_H */
