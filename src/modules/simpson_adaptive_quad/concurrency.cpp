/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Adaptive Simpson Numerical Quadrature Integrator.
 * Module: simpson_adaptive_quad
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct simpson_adaptive_quad_reentrant_lock {
    volatile uint64_t sequence;
    volatile uint32_t concurrency_count;
} simpson_adaptive_quad_reentrant_lock_t;

static inline void simpson_adaptive_quad_seq_advance(simpson_adaptive_quad_reentrant_lock_t* lk) {
    __atomic_fetch_add(&lk->sequence, 1, __ATOMIC_RELEASE);
}
