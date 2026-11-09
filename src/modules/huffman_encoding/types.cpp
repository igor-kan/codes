/**
 * @file types.cpp
 * @brief Core types and configuration for Canonical Huffman Tree and Variable-Length Encoder.
 * Module: huffman_encoding
 */

#ifndef HUFFMAN_ENCODING_TYPES_H
#define HUFFMAN_ENCODING_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define HUFFMAN_ENCODING_ALIGNMENT 64
#define HUFFMAN_ENCODING_CAPACITY 2048

typedef struct huffman_encoding_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} huffman_encoding_config_t;

typedef struct huffman_encoding_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    huffman_encoding_config_t config;
} huffman_encoding_state_t;

#endif /* HUFFMAN_ENCODING_TYPES_H */
