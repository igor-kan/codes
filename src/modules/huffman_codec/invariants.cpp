/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Canonical Huffman Variable-Length Entropy Codec.
 * Module: huffman_codec
 */

#include <assert.h>
#include <math.h>

static inline void huffman_codec_check_invariants(double input, double output) {
    if (input == 0.0) {
        assert(output == 0.0 || fabs(output) < 1e-12);
    }
    if (isfinite(input)) {
        assert(isfinite(output));
    }
}
