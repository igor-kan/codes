/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Heavy-Light Decomposition for Tree Path Invariant Queries.
 * Module: heavy_light_decomp
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct heavy_light_decomp_sync_counter {
    volatile uint64_t count;
} heavy_light_decomp_sync_counter_t;

static inline void heavy_light_decomp_sync_inc(heavy_light_decomp_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
