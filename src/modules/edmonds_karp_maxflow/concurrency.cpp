/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Edmonds-Karp Maximum Bipartite Network Flow Engine.
 * Module: edmonds_karp_maxflow
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct edmonds_karp_maxflow_sync_state {
    volatile uint64_t counter;
    volatile uint32_t concurrency_count;
} edmonds_karp_maxflow_sync_state_t;

static inline void edmonds_karp_maxflow_sync_increment(edmonds_karp_maxflow_sync_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELEASE);
}
