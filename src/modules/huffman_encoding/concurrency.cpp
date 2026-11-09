/**
 * @file concurrency.cpp
 * @brief Thread safety and reentrancy model for Canonical Huffman Tree and Variable-Length Encoder.
 * Module: huffman_encoding
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct huffman_encoding_sync_counter {
    volatile uint64_t count;
} huffman_encoding_sync_counter_t;

static inline void huffman_encoding_sync_inc(huffman_encoding_sync_counter_t* c) {
    __atomic_fetch_add(&c->count, 1, __ATOMIC_RELAXED);
}
