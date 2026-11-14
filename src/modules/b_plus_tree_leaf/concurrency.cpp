/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Leaf-Chained B+ Tree Index Structure for Range Scans.
 * Module: b_plus_tree_leaf
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct b_plus_tree_leaf_sync_state {
    volatile uint64_t counter;
    volatile uint32_t concurrency_count;
} b_plus_tree_leaf_sync_state_t;

static inline void b_plus_tree_leaf_sync_increment(b_plus_tree_leaf_sync_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELEASE);
}
