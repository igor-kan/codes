/**
 * @file types.cpp
 * @brief Core types and configuration for Dense Cholesky Factorization with Positive-Definite Check.
 * Module: matrix_cholesky_dense
 */

#ifndef MATRIX_CHOLESKY_DENSE_TYPES_H
#define MATRIX_CHOLESKY_DENSE_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define MATRIX_CHOLESKY_DENSE_ALIGNMENT 64
#define MATRIX_CHOLESKY_DENSE_DEFAULT_SZ 8192

typedef struct matrix_cholesky_dense_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} matrix_cholesky_dense_config_t;

typedef struct matrix_cholesky_dense_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    matrix_cholesky_dense_config_t config;
} matrix_cholesky_dense_state_t;

#endif /* MATRIX_CHOLESKY_DENSE_TYPES_H */
