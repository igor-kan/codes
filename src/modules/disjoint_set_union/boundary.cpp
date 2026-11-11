/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Disjoint-Set Union (DSU) with Path Compression and Rank.
 * Module: disjoint_set_union
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool disjoint_set_union_is_valid_float(double x) {
    return isfinite(x);
}

static inline double disjoint_set_union_clamp_input(double x, double min_val, double max_val) {
    if (!isfinite(x)) return 0.0;
    if (x < min_val) return min_val;
    if (x > max_val) return max_val;
    return x;
}
