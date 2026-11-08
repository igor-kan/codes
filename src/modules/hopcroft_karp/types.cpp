/**
 * @file types.cpp
 * @brief Core type definitions and operational interfaces for Hopcroft-Karp Maximum Bipartite Matching.
 * Module: hopcroft_karp
 */

#ifndef HOPCROFT_KARP_TYPES_H
#define HOPCROFT_KARP_TYPES_H

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define HOPCROFT_KARP_ALIGNMENT 64
#define HOPCROFT_KARP_SUCCESS 0
#define HOPCROFT_KARP_ERR_NULL_PTR -1
#define HOPCROFT_KARP_ERR_INVALID_PARAM -2
#define HOPCROFT_KARP_ERR_OUT_OF_BOUNDS -3

typedef struct hopcroft_karp_config {
    size_t capacity;
    uint32_t flags;
    double tolerance;
} hopcroft_karp_config_t;

typedef struct hopcroft_karp_context {
    void* buffer;
    size_t size;
    size_t capacity;
    uint64_t operations_count;
    hopcroft_karp_config_t config;
} hopcroft_karp_context_t;

int hopcroft_karp_init(hopcroft_karp_context_t* ctx, const hopcroft_karp_config_t* cfg);
int hopcroft_karp_destroy(hopcroft_karp_context_t* ctx);

#ifdef __cplusplus
}
#endif

#endif /* HOPCROFT_KARP_TYPES_H */
