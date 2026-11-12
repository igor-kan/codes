/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Graham Scan 2D Convex Hull Vectorized Geometry.
 * Module: graham_scan_2d
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct graham_scan_2d_atomic_state {
    volatile uint64_t counter;
    volatile uint32_t active_threads;
} graham_scan_2d_atomic_state_t;

static inline void graham_scan_2d_atomic_increment(graham_scan_2d_atomic_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELAXED);
}
