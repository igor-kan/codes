/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Dense Cholesky Factorization with Positive-Definite Check.
 * Module: matrix_cholesky_dense
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct matrix_cholesky_dense_sync_counter {
    volatile uint64_t count;
} matrix_cholesky_dense_sync_counter_t;

static inline void matrix_cholesky_dense_sync_inc_v47(matrix_cholesky_dense_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
