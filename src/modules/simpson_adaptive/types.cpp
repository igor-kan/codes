/**
 * @file types.cpp
 * @brief Core type definitions and operational interfaces for Adaptive Quadrature Numerical Integrator.
 * Module: simpson_adaptive
 */

#ifndef SIMPSON_ADAPTIVE_TYPES_H
#define SIMPSON_ADAPTIVE_TYPES_H

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define SIMPSON_ADAPTIVE_ALIGNMENT 64
#define SIMPSON_ADAPTIVE_SUCCESS 0
#define SIMPSON_ADAPTIVE_ERR_NULL_PTR -1
#define SIMPSON_ADAPTIVE_ERR_INVALID_PARAM -2
#define SIMPSON_ADAPTIVE_ERR_OUT_OF_BOUNDS -3

typedef struct simpson_adaptive_config {
    size_t capacity;
    uint32_t flags;
    double tolerance;
} simpson_adaptive_config_t;

typedef struct simpson_adaptive_context {
    void* buffer;
    size_t size;
    size_t capacity;
    uint64_t operations_count;
    simpson_adaptive_config_t config;
} simpson_adaptive_context_t;

int simpson_adaptive_init(simpson_adaptive_context_t* ctx, const simpson_adaptive_config_t* cfg);
int simpson_adaptive_destroy(simpson_adaptive_context_t* ctx);

#ifdef __cplusplus
}
#endif

#endif /* SIMPSON_ADAPTIVE_TYPES_H */
