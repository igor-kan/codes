/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Monotone Chain (Andrew Algorithm) 2D Convex Hull.
 * Module: convex_hull_monotone
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool convex_hull_monotone_is_valid_float(double x) {
    return isfinite(x);
}

static inline double convex_hull_monotone_clamp_input(double x, double min_val, double max_val) {
    if (!isfinite(x)) return 0.0;
    if (x < min_val) return min_val;
    if (x > max_val) return max_val;
    return x;
}
