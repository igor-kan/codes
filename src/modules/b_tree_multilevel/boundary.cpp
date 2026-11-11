/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Multi-Level Balanced B-Tree with Node Split-Merge.
 * Module: b_tree_multilevel
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool b_tree_multilevel_is_valid_float(double x) {
    return isfinite(x);
}

static inline double b_tree_multilevel_clamp_input(double x, double min_val, double max_val) {
    if (!isfinite(x)) return 0.0;
    if (x < min_val) return min_val;
    if (x > max_val) return max_val;
    return x;
}
