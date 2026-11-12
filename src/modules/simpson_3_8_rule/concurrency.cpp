/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Composite Simpson 3/8 Rule Numerical Integrator.
 * Module: simpson_3_8_rule
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct simpson_3_8_rule_atomic_state {
    volatile uint64_t counter;
    volatile uint32_t active_threads;
} simpson_3_8_rule_atomic_state_t;

static inline void simpson_3_8_rule_atomic_increment(simpson_3_8_rule_atomic_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELAXED);
}
