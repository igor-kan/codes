/**
 * @file concurrency.cpp
 * @brief Thread-safe reentrancy and atomic state primitives for Canonical Huffman Variable-Length Entropy Codec.
 * Module: huffman_codec
 */

#include <stdint.h>
#include <stdbool.h>

typedef struct huffman_codec_atomic_state {
    volatile uint64_t counter;
    volatile uint32_t active_threads;
} huffman_codec_atomic_state_t;

static inline void huffman_codec_atomic_increment(huffman_codec_atomic_state_t* s) {
    __atomic_fetch_add(&s->counter, 1, __ATOMIC_RELAXED);
}
