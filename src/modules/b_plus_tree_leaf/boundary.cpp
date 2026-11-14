/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for Leaf-Chained B+ Tree Index Structure for Range Scans.
 * Module: b_plus_tree_leaf
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool b_plus_tree_leaf_is_finite_val(double v) {
    return isfinite(v);
}

static inline double b_plus_tree_leaf_clamp_val(double v, double min_v, double max_v) {
    if (!isfinite(v)) return 0.0;
    if (v < min_v) return min_v;
    if (v > max_v) return max_v;
    return v;
}
