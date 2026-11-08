/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Tarjan Strongly Connected Components Low-Link Graph Engine.
 * Module: tarjan_scc
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct tarjan_scc_atomic_counter {
    volatile uint64_t value;
} tarjan_scc_atomic_counter_t;

static inline void tarjan_scc_counter_inc(tarjan_scc_atomic_counter_t* c) {
    __atomic_fetch_add(&c->value, 1, __ATOMIC_RELAXED);
}
