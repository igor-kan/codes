/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Tarjan Strongly Connected Components Low-Link Graph Engine.
 * Module: tarjan_scc
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool tarjan_scc_is_valid_float(double x) {
    return isfinite(x);
}

static inline double tarjan_scc_sanitize_input(double x, double min_bound, double max_bound) {
    if (!isfinite(x)) return 0.0;
    if (x < min_bound) return min_bound;
    if (x > max_bound) return max_bound;
    return x;
}
