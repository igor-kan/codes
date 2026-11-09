/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Dinic Maximum Flow Network with Level Graphs.
 * Module: max_flow_dinic
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct max_flow_dinic_sync_counter {
    volatile uint64_t count;
} max_flow_dinic_sync_counter_t;

static inline void max_flow_dinic_sync_inc(max_flow_dinic_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
