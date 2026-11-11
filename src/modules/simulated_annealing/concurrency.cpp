/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Continuous Domain Simulated Annealing Global Optimizer.
 * Module: simulated_annealing
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct simulated_annealing_sync_counter {
    volatile uint64_t count;
} simulated_annealing_sync_counter_t;

static inline void simulated_annealing_sync_inc_v47(simulated_annealing_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
