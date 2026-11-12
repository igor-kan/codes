/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Canonical Huffman Variable-Length Entropy Codec.
 * Module: huffman_codec | Algorithm Family: compression
 */

#ifndef HUFFMAN_CODEC_TYPES_H
#define HUFFMAN_CODEC_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define HUFFMAN_CODEC_ALIGNMENT 64
#define HUFFMAN_CODEC_BASE_CAPACITY 1024

typedef struct huffman_codec_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} huffman_codec_config_t;

typedef struct huffman_codec_state {
    void* buffer;
    size_t count;
    uint64_t operations;
    double accumulator;
    huffman_codec_config_t config;
} huffman_codec_state_t;

#endif /* HUFFMAN_CODEC_TYPES_H */
