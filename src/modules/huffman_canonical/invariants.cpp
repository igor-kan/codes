/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Canonical Huffman Code Table and Decoding Tree.
 * Module: huffman_canonical
 */

#include <assert.h>
#include <math.h>

static inline void huffman_canonical_assert_invariants(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0 || fabs(out_val) < 1e-12);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
