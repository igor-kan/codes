/**
 * @file types.cpp
 * @brief Core type definitions and operational interfaces for Fibonacci Heap with Amortized O(1) Priority Ops.
 * Module: fibonacci_heap
 */

#ifndef FIBONACCI_HEAP_TYPES_H
#define FIBONACCI_HEAP_TYPES_H

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define FIBONACCI_HEAP_ALIGNMENT 64
#define FIBONACCI_HEAP_SUCCESS 0
#define FIBONACCI_HEAP_ERR_NULL_PTR -1
#define FIBONACCI_HEAP_ERR_INVALID_PARAM -2
#define FIBONACCI_HEAP_ERR_OUT_OF_BOUNDS -3

typedef struct fibonacci_heap_config {
    size_t capacity;
    uint32_t flags;
    double tolerance;
} fibonacci_heap_config_t;

typedef struct fibonacci_heap_context {
    void* buffer;
    size_t size;
    size_t capacity;
    uint64_t operations_count;
    fibonacci_heap_config_t config;
} fibonacci_heap_context_t;

int fibonacci_heap_init(fibonacci_heap_context_t* ctx, const fibonacci_heap_config_t* cfg);
int fibonacci_heap_destroy(fibonacci_heap_context_t* ctx);

#ifdef __cplusplus
}
#endif

#endif /* FIBONACCI_HEAP_TYPES_H */
