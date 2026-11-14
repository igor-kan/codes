/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Boole 5-Point Closed Newton-Cotes Numerical Quadrature.
 * Module: simpson_boole_quadrature
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct simpson_boole_quadrature_sync_state {
    volatile uint64_t counter;
    volatile uint32_t concurrency_count;
} simpson_boole_quadrature_sync_state_t;

static inline void simpson_boole_quadrature_sync_increment(simpson_boole_quadrature_sync_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELEASE);
}
