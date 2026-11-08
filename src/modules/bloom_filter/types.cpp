/**
 * @file types.cpp
 * @brief Core type definitions and operational interfaces for Murmur3-Seeded High-Density Bloom Filter.
 * Module: bloom_filter
 */

#ifndef BLOOM_FILTER_TYPES_H
#define BLOOM_FILTER_TYPES_H

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BLOOM_FILTER_ALIGNMENT 64
#define BLOOM_FILTER_SUCCESS 0
#define BLOOM_FILTER_ERR_NULL_PTR -1
#define BLOOM_FILTER_ERR_INVALID_PARAM -2
#define BLOOM_FILTER_ERR_OUT_OF_BOUNDS -3

typedef struct bloom_filter_config {
    size_t capacity;
    uint32_t flags;
    double tolerance;
} bloom_filter_config_t;

typedef struct bloom_filter_context {
    void* buffer;
    size_t size;
    size_t capacity;
    uint64_t operations_count;
    bloom_filter_config_t config;
} bloom_filter_context_t;

int bloom_filter_init(bloom_filter_context_t* ctx, const bloom_filter_config_t* cfg);
int bloom_filter_destroy(bloom_filter_context_t* ctx);

#ifdef __cplusplus
}
#endif

#endif /* BLOOM_FILTER_TYPES_H */
