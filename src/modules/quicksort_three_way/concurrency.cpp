/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Dijkstra 3-Way Partitioning Quicksort for Duplicates.
 * Module: quicksort_three_way
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct quicksort_three_way_sync_state {
    volatile uint64_t counter;
    volatile uint32_t concurrency_count;
} quicksort_three_way_sync_state_t;

static inline void quicksort_three_way_sync_increment(quicksort_three_way_sync_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELEASE);
}
