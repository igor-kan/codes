/**
 * Boundary condition checking and IEEE-754 edge-case handlers for Graham Scan 2D Convex Hull with Cross Products.
 * Module: convex_hull_graham
 */

#ifndef BOUNDARY_CONVEX_HULL_GRAHAM_H
#define BOUNDARY_CONVEX_HULL_GRAHAM_H

#include <math.h>
#include <stdbool.h>

static inline bool convex_hull_graham_is_finite_input(double x) {
    return isfinite(x);
}

static inline double convex_hull_graham_clamp(double val, double min_val, double max_val) {
    const double t = val < min_val ? min_val : val;
    return t > max_val ? max_val : t;
}

#endif /* BOUNDARY_CONVEX_HULL_GRAHAM_H */
