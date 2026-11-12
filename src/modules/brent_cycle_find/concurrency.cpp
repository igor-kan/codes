/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Brent Teleporting Tortoise and Hare Cycle Detector.
 * Module: brent_cycle_find
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct brent_cycle_find_atomic_state {
    volatile uint64_t counter;
    volatile uint32_t active_threads;
} brent_cycle_find_atomic_state_t;

static inline void brent_cycle_find_atomic_increment(brent_cycle_find_atomic_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELAXED);
}
