/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Canonical Huffman Variable-Length Entropy Codec.
 * Module: huffman_codec | Algorithm Family: compression
 */

#ifndef HUFFMAN_CODEC_INTERFACE_H
#define HUFFMAN_CODEC_INTERFACE_H

#include "types.cpp"

typedef int (*huffman_codec_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct huffman_codec_vtable {
    int (*init)(huffman_codec_state_t* state, const huffman_codec_config_t* cfg);
    int (*execute)(huffman_codec_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(huffman_codec_state_t* state);
    int (*destroy)(huffman_codec_state_t* state);
} huffman_codec_vtable_t;

#endif /* HUFFMAN_CODEC_INTERFACE_H */
