/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Manacher Linear-Time Longest Palindromic Substring.
 * Module: manacher_palindrome
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct manacher_palindrome_reentrant_lock {
    volatile uint64_t sequence;
    volatile uint32_t concurrency_count;
} manacher_palindrome_reentrant_lock_t;

static inline void manacher_palindrome_seq_advance(manacher_palindrome_reentrant_lock_t* lk) {
    __atomic_fetch_add(&lk->sequence, 1, __ATOMIC_RELEASE);
}
