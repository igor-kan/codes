/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for Rabin-Karp Rolling Hash Substring Matcher.
 * Module: rabin_karp_search
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool rabin_karp_search_is_finite(double v) {
    return isfinite(v);
}

static inline double rabin_karp_search_clamp_range(double v, double lo, double hi) {
    if (!isfinite(v)) return 0.0;
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
}
