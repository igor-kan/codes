/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Goldberg-Tarjan Push-Relabel Maximum Flow Network.
 * Module: push_relabel_maxflow
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool push_relabel_maxflow_is_valid_float(double x) {
    return isfinite(x);
}

static inline double push_relabel_maxflow_clamp_input(double x, double min_val, double max_val) {
    if (!isfinite(x)) return 0.0;
    if (x < min_val) return min_val;
    if (x > max_val) return max_val;
    return x;
}
