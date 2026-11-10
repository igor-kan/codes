/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for R*-Tree Spatial Index with Topological Reinsertion.
 * Module: spatial_rtree_star
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct spatial_rtree_star_sync_counter {
    volatile uint64_t count;
} spatial_rtree_star_sync_counter_t;

static inline void spatial_rtree_star_sync_inc(spatial_rtree_star_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
