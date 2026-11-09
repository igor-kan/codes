/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Linear-Time Suffix Automaton Substring Engine.
 * Module: suffix_automaton
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct suffix_automaton_sync_counter {
    volatile uint64_t count;
} suffix_automaton_sync_counter_t;

static inline void suffix_automaton_sync_inc(suffix_automaton_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
