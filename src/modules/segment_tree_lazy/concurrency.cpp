/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Segment Tree with Lazy Propagation Range Updates.
 * Module: segment_tree_lazy
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct segment_tree_lazy_sync_counter {
    volatile uint64_t count;
} segment_tree_lazy_sync_counter_t;

static inline void segment_tree_lazy_sync_inc(segment_tree_lazy_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
