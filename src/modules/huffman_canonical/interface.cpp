/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Canonical Huffman Code Table and Decoding Tree.
 * Module: huffman_canonical | Algorithm Family: compression
 */

#ifndef HUFFMAN_CANONICAL_INTERFACE_H
#define HUFFMAN_CANONICAL_INTERFACE_H

#include "types.cpp"

typedef int (*huffman_canonical_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct huffman_canonical_vtable {
    int (*init)(huffman_canonical_state_t* state, const huffman_canonical_config_t* cfg);
    int (*execute)(huffman_canonical_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(huffman_canonical_state_t* state);
    int (*destroy)(huffman_canonical_state_t* state);
} huffman_canonical_vtable_t;

#endif /* HUFFMAN_CANONICAL_INTERFACE_H */
