/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Manber-Myers O(N log N) Suffix Array Construction.
 * Module: suffix_array_manber
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct suffix_array_manber_sync_state {
    volatile uint64_t counter;
    volatile uint32_t concurrency_count;
} suffix_array_manber_sync_state_t;

static inline void suffix_array_manber_sync_increment(suffix_array_manber_sync_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELEASE);
}
