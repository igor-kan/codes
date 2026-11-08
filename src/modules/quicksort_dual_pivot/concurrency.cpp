/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Yaroslavskiy Dual-Pivot Vectorized Quicksort.
 * Module: quicksort_dual_pivot
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct quicksort_dual_pivot_atomic_counter {
    volatile uint64_t value;
} quicksort_dual_pivot_atomic_counter_t;

static inline void quicksort_dual_pivot_counter_inc(quicksort_dual_pivot_atomic_counter_t* c) {
    __atomic_fetch_add(&c->value, 1, __ATOMIC_RELAXED);
}
