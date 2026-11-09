/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Strassen Sub-Cubic Fast Matrix Multiplication.
 * Module: matrix_strassen
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct matrix_strassen_sync_counter {
    volatile uint64_t count;
} matrix_strassen_sync_counter_t;

static inline void matrix_strassen_sync_inc(matrix_strassen_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
