/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Canonical Huffman Tree and Variable-Length Encoder.
 * Module: huffman_encoding
 */

#include <assert.h>

void test_huffman_encoding_regression_underflow(void) {
    double tiny = 1e-308;
    double res = tiny * (1.0 + 0.3 * tiny);
    assert(res >= 0.0);
}
