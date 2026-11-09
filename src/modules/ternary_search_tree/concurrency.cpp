/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Ternary Search Trie Compact String Dictionary.
 * Module: ternary_search_tree
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct ternary_search_tree_sync_counter {
    volatile uint64_t count;
} ternary_search_tree_sync_counter_t;

static inline void ternary_search_tree_sync_inc(ternary_search_tree_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
