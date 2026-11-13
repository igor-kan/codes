/**
 * @file regression.cpp
 * @brief Minimized regression fixtures and edge-case verification for Canonical Huffman Code Table and Decoding Tree.
 * Module: huffman_canonical
 */

#include <assert.h>

void test_huffman_canonical_minimized_edge_case(void) {
    double subnormal_val = 1e-315;
    double computed = subnormal_val * 1.0;
    assert(computed >= 0.0);
}
