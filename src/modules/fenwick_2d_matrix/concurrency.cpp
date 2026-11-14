/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for 2D Binary Indexed Tree (Fenwick Matrix) Range Updater.
 * Module: fenwick_2d_matrix
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct fenwick_2d_matrix_sync_state {
    volatile uint64_t counter;
    volatile uint32_t concurrency_count;
} fenwick_2d_matrix_sync_state_t;

static inline void fenwick_2d_matrix_sync_increment(fenwick_2d_matrix_sync_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELEASE);
}
