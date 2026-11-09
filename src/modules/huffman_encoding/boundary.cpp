/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Canonical Huffman Tree and Variable-Length Encoder.
 * Module: huffman_encoding
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool huffman_encoding_is_valid_float(double x) {
    return isfinite(x);
}

static inline double huffman_encoding_clamp_input(double x, double min_val, double max_val) {
    if (!isfinite(x)) return 0.0;
    if (x < min_val) return min_val;
    if (x > max_val) return max_val;
    return x;
}
