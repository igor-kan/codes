/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Monotone Chain (Andrew Algorithm) 2D Convex Hull.
 * Module: convex_hull_monotone
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct convex_hull_monotone_sync_counter {
    volatile uint64_t count;
} convex_hull_monotone_sync_counter_t;

static inline void convex_hull_monotone_sync_inc_v47(convex_hull_monotone_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
