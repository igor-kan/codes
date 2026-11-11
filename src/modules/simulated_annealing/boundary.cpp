/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Continuous Domain Simulated Annealing Global Optimizer.
 * Module: simulated_annealing
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool simulated_annealing_is_valid_float(double x) {
    return isfinite(x);
}

static inline double simulated_annealing_clamp_input(double x, double min_val, double max_val) {
    if (!isfinite(x)) return 0.0;
    if (x < min_val) return min_val;
    if (x > max_val) return max_val;
    return x;
}
