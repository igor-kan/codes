/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Aho-Corasick Multi-Pattern String Matching Automaton.
 * Module: aho_corasick_automaton
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct aho_corasick_automaton_sync_counter {
    volatile uint64_t count;
} aho_corasick_automaton_sync_counter_t;

static inline void aho_corasick_automaton_sync_inc_v47(aho_corasick_automaton_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
