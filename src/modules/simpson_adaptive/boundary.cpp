/**
 * Boundary condition checking and IEEE-754 edge-case handlers for Adaptive Quadrature Numerical Integrator.
 * Module: simpson_adaptive
 */

#ifndef BOUNDARY_SIMPSON_ADAPTIVE_H
#define BOUNDARY_SIMPSON_ADAPTIVE_H

#include <math.h>
#include <stdbool.h>

static inline bool simpson_adaptive_is_finite_input(double x) {
    return isfinite(x);
}

static inline double simpson_adaptive_clamp(double val, double min_val, double max_val) {
    const double t = val < min_val ? min_val : val;
    return t > max_val ? max_val : t;
}

#endif /* BOUNDARY_SIMPSON_ADAPTIVE_H */
