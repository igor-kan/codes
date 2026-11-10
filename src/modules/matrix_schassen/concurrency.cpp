/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Schonhage-Strassen Fast Integer & Polynomial Multiply.
 * Module: matrix_schassen
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct matrix_schassen_sync_counter {
    volatile uint64_t count;
} matrix_schassen_sync_counter_t;

static inline void matrix_schassen_sync_inc(matrix_schassen_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
