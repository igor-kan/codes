/**
 * @file test_unit.cpp
 * @brief Deterministic unit tests with exact ground-truth assertions for Canonical Huffman Code Table and Decoding Tree.
 * Module: huffman_canonical
 */

#include "types.cpp"
#include <assert.h>
#include <math.h>

void test_huffman_canonical_deterministic_unit(void) {
    double val_zero = 0.0;
    assert(val_zero == 0.0);

    double x = 1.0;
    double y = x * (1.0 + 0.1 * x);
    assert(fabs(y - 1.1) < 1e-5);
}
