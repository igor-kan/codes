/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for Canonical Huffman Variable-Length Entropy Codec.
 * Module: huffman_codec
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool huffman_codec_is_finite(double v) {
    return isfinite(v);
}

static inline double huffman_codec_clamp_range(double v, double lo, double hi) {
    if (!isfinite(v)) return 0.0;
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
}
