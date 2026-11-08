/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Self-Balancing AVL Search Tree with Rotations.
 * Module: avl_balanced_tree
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct avl_balanced_tree_atomic_counter {
    volatile uint64_t value;
} avl_balanced_tree_atomic_counter_t;

static inline void avl_balanced_tree_counter_inc(avl_balanced_tree_atomic_counter_t* c) {
    __atomic_fetch_add(&c->value, 1, __ATOMIC_RELAXED);
}
