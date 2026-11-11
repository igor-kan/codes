/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Karatsuba Divide-and-Conquer Polynomial Multiplication.
 * Module: karatsuba_poly_mul
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct karatsuba_poly_mul_sync_counter {
    volatile uint64_t count;
} karatsuba_poly_mul_sync_counter_t;

static inline void karatsuba_poly_mul_sync_inc_v47(karatsuba_poly_mul_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
