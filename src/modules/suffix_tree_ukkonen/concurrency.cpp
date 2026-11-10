/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Ukkonen Linear-Time Online Suffix Tree Construction.
 * Module: suffix_tree_ukkonen
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct suffix_tree_ukkonen_sync_counter {
    volatile uint64_t count;
} suffix_tree_ukkonen_sync_counter_t;

static inline void suffix_tree_ukkonen_sync_inc(suffix_tree_ukkonen_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
