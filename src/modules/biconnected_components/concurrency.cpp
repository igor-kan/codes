/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Hopcroft-Tarjan Articulation Points and Bridges.
 * Module: biconnected_components
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct biconnected_components_sync_counter {
    volatile uint64_t count;
} biconnected_components_sync_counter_t;

static inline void biconnected_components_sync_inc(biconnected_components_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
