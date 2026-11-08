/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Dijkstra Shortest Path with Fibonacci Priority Queue.
 * Module: dijkstra_fibonacci
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct dijkstra_fibonacci_atomic_counter {
    volatile uint64_t value;
} dijkstra_fibonacci_atomic_counter_t;

static inline void dijkstra_fibonacci_counter_inc(dijkstra_fibonacci_atomic_counter_t* c) {
    __atomic_fetch_add(&c->value, 1, __ATOMIC_RELAXED);
}
