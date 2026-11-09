/**
 * @file interface.cpp
 * @brief Abstract contracts and prototypes for Canonical Huffman Tree and Variable-Length Encoder.
 * Module: huffman_encoding
 */

#ifndef HUFFMAN_ENCODING_INTERFACE_H
#define HUFFMAN_ENCODING_INTERFACE_H

#include "types.cpp"

typedef int (*huffman_encoding_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct huffman_encoding_vtable {
    int (*init)(huffman_encoding_state_t* state, const huffman_encoding_config_t* cfg);
    int (*execute)(huffman_encoding_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*destroy)(huffman_encoding_state_t* state);
} huffman_encoding_vtable_t;

#endif /* HUFFMAN_ENCODING_INTERFACE_H */
