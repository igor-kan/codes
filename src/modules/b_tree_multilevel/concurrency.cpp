/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Multi-Level Balanced B-Tree with Node Split-Merge.
 * Module: b_tree_multilevel
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct b_tree_multilevel_sync_counter {
    volatile uint64_t count;
} b_tree_multilevel_sync_counter_t;

static inline void b_tree_multilevel_sync_inc_v47(b_tree_multilevel_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
