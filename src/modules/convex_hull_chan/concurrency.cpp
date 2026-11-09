/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Chan Optimal 2D Convex Hull Geometric Engine.
 * Module: convex_hull_chan
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct convex_hull_chan_sync_counter {
    volatile uint64_t count;
} convex_hull_chan_sync_counter_t;

static inline void convex_hull_chan_sync_inc(convex_hull_chan_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
