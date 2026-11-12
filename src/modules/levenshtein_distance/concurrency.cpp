/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Wagner-Fischer Dynamic Programming Edit Distance.
 * Module: levenshtein_distance
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct levenshtein_distance_atomic_state {
    volatile uint64_t counter;
    volatile uint32_t active_threads;
} levenshtein_distance_atomic_state_t;

static inline void levenshtein_distance_atomic_increment(levenshtein_distance_atomic_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELAXED);
}
