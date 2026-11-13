/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for Adaptive Simpson Numerical Quadrature Integrator.
 * Module: simpson_adaptive_quad
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool simpson_adaptive_quad_check_finite(double v) {
    return isfinite(v);
}

static inline double simpson_adaptive_quad_bound_clamp(double v, double min_v, double max_v) {
    if (!isfinite(v)) return 0.0;
    if (v < min_v) return min_v;
    if (v > max_v) return max_v;
    return v;
}
