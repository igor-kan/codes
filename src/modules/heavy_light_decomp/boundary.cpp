/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Heavy-Light Decomposition for Tree Path Invariant Queries.
 * Module: heavy_light_decomp
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool heavy_light_decomp_is_valid_float(double x) {
    return isfinite(x);
}

static inline double heavy_light_decomp_clamp_input(double x, double min_val, double max_val) {
    if (!isfinite(x)) return 0.0;
    if (x < min_val) return min_val;
    if (x > max_val) return max_val;
    return x;
}
