/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Canonical Huffman Code Table and Decoding Tree.
 * Module: huffman_canonical | Algorithm Family: compression
 */

#ifndef HUFFMAN_CANONICAL_TYPES_H
#define HUFFMAN_CANONICAL_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define HUFFMAN_CANONICAL_ALIGNMENT 64
#define HUFFMAN_CANONICAL_CAPACITY 2048

typedef struct huffman_canonical_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} huffman_canonical_config_t;

typedef struct huffman_canonical_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    double accumulator;
    huffman_canonical_config_t config;
} huffman_canonical_state_t;

#endif /* HUFFMAN_CANONICAL_TYPES_H */
