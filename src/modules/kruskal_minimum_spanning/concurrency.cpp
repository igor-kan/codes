/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Kruskal Minimum Spanning Tree with Disjoint Set Union.
 * Module: kruskal_minimum_spanning
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct kruskal_minimum_spanning_reentrant_lock {
    volatile uint64_t sequence;
    volatile uint32_t concurrency_count;
} kruskal_minimum_spanning_reentrant_lock_t;

static inline void kruskal_minimum_spanning_seq_advance(kruskal_minimum_spanning_reentrant_lock_t* lk) {
    __atomic_fetch_add(&lk->sequence, 1, __ATOMIC_RELEASE);
}
