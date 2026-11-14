/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for 2D Binary Indexed Tree (Fenwick Matrix) Range Updater.
 * Module: fenwick_2d_matrix
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool fenwick_2d_matrix_is_finite_val(double v) {
    return isfinite(v);
}

static inline double fenwick_2d_matrix_clamp_val(double v, double min_v, double max_v) {
    if (!isfinite(v)) return 0.0;
    if (v < min_v) return min_v;
    if (v > max_v) return max_v;
    return v;
}
