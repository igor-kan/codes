/**
 * @file types.cpp
 * @brief Core types and configuration for Karatsuba Divide-and-Conquer Polynomial Multiplication.
 * Module: karatsuba_poly_mul
 */

#ifndef KARATSUBA_POLY_MUL_TYPES_H
#define KARATSUBA_POLY_MUL_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define KARATSUBA_POLY_MUL_ALIGNMENT 64
#define KARATSUBA_POLY_MUL_DEFAULT_SZ 8192

typedef struct karatsuba_poly_mul_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} karatsuba_poly_mul_config_t;

typedef struct karatsuba_poly_mul_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    karatsuba_poly_mul_config_t config;
} karatsuba_poly_mul_state_t;

#endif /* KARATSUBA_POLY_MUL_TYPES_H */
