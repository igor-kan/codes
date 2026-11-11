/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Disjoint-Set Union (DSU) with Path Compression and Rank.
 * Module: disjoint_set_union
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct disjoint_set_union_sync_counter {
    volatile uint64_t count;
} disjoint_set_union_sync_counter_t;

static inline void disjoint_set_union_sync_inc_v47(disjoint_set_union_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
