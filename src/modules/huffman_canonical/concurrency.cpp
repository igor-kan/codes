/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Canonical Huffman Code Table and Decoding Tree.
 * Module: huffman_canonical
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct huffman_canonical_reentrant_lock {
    volatile uint64_t sequence;
    volatile uint32_t concurrency_count;
} huffman_canonical_reentrant_lock_t;

static inline void huffman_canonical_seq_advance(huffman_canonical_reentrant_lock_t* lk) {
    __atomic_fetch_add(&lk->sequence, 1, __ATOMIC_RELEASE);
}
