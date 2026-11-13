/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for Canonical Huffman Code Table and Decoding Tree.
 * Module: huffman_canonical
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool huffman_canonical_check_finite(double v) {
    return isfinite(v);
}

static inline double huffman_canonical_bound_clamp(double v, double min_v, double max_v) {
    if (!isfinite(v)) return 0.0;
    if (v < min_v) return min_v;
    if (v > max_v) return max_v;
    return v;
}
