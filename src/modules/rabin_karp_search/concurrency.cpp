/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Rabin-Karp Rolling Hash Substring Matcher.
 * Module: rabin_karp_search
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct rabin_karp_search_atomic_state {
    volatile uint64_t counter;
    volatile uint32_t active_threads;
} rabin_karp_search_atomic_state_t;

static inline void rabin_karp_search_atomic_increment(rabin_karp_search_atomic_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELAXED);
}
