/**
 * @file types.cpp
 * @brief Core type definitions and operational interfaces for Parallel Cache-Conscious Radix Sort Engine.
 * Module: radix_sort_engine
 */

#ifndef RADIX_SORT_ENGINE_TYPES_H
#define RADIX_SORT_ENGINE_TYPES_H

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define RADIX_SORT_ENGINE_ALIGNMENT 64
#define RADIX_SORT_ENGINE_SUCCESS 0
#define RADIX_SORT_ENGINE_ERR_NULL_PTR -1
#define RADIX_SORT_ENGINE_ERR_INVALID_PARAM -2
#define RADIX_SORT_ENGINE_ERR_OUT_OF_BOUNDS -3

typedef struct radix_sort_engine_config {
    size_t capacity;
    uint32_t flags;
    double tolerance;
} radix_sort_engine_config_t;

typedef struct radix_sort_engine_context {
    void* buffer;
    size_t size;
    size_t capacity;
    uint64_t operations_count;
    radix_sort_engine_config_t config;
} radix_sort_engine_context_t;

int radix_sort_engine_init(radix_sort_engine_context_t* ctx, const radix_sort_engine_config_t* cfg);
int radix_sort_engine_destroy(radix_sort_engine_context_t* ctx);

#ifdef __cplusplus
}
#endif

#endif /* RADIX_SORT_ENGINE_TYPES_H */
