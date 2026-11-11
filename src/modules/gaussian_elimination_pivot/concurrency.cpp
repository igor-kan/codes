/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Gaussian Elimination with Scaled Partial Pivoting.
 * Module: gaussian_elimination_pivot
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct gaussian_elimination_pivot_sync_counter {
    volatile uint64_t count;
} gaussian_elimination_pivot_sync_counter_t;

static inline void gaussian_elimination_pivot_sync_inc_v47(gaussian_elimination_pivot_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
