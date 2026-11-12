/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for Wagner-Fischer Dynamic Programming Edit Distance.
 * Module: levenshtein_distance
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool levenshtein_distance_is_finite(double v) {
    return isfinite(v);
}

static inline double levenshtein_distance_clamp_range(double v, double lo, double hi) {
    if (!isfinite(v)) return 0.0;
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
}
