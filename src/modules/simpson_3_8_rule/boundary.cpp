/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for Composite Simpson 3/8 Rule Numerical Integrator.
 * Module: simpson_3_8_rule
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool simpson_3_8_rule_is_finite(double v) {
    return isfinite(v);
}

static inline double simpson_3_8_rule_clamp_range(double v, double lo, double hi) {
    if (!isfinite(v)) return 0.0;
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
}
