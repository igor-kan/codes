/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Multi-Dimensional K-d Tree Nearest Neighbor Engine.
 * Module: kdtree_spatial
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct kdtree_spatial_atomic_counter {
    volatile uint64_t value;
} kdtree_spatial_atomic_counter_t;

static inline void kdtree_spatial_counter_inc(kdtree_spatial_atomic_counter_t* c) {
    __atomic_fetch_add(&c->value, 1, __ATOMIC_RELAXED);
}
