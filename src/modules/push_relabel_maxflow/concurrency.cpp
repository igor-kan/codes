/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Goldberg-Tarjan Push-Relabel Maximum Flow Network.
 * Module: push_relabel_maxflow
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct push_relabel_maxflow_sync_counter {
    volatile uint64_t count;
} push_relabel_maxflow_sync_counter_t;

static inline void push_relabel_maxflow_sync_inc(push_relabel_maxflow_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
