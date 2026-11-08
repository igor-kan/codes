/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Multi-Dimensional K-d Tree Nearest Neighbor Engine.
 * Module: kdtree_spatial
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool kdtree_spatial_is_valid_float(double x) {
    return isfinite(x);
}

static inline double kdtree_spatial_sanitize_input(double x, double min_bound, double max_bound) {
    if (!isfinite(x)) return 0.0;
    if (x < min_bound) return min_bound;
    if (x > max_bound) return max_bound;
    return x;
}
