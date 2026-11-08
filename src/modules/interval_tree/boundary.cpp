/**
 * Boundary condition checking and IEEE-754 edge-case handlers for Augmented Red-Black Interval Stabbing Tree.
 * Module: interval_tree
 */

#ifndef BOUNDARY_INTERVAL_TREE_H
#define BOUNDARY_INTERVAL_TREE_H

#include <math.h>
#include <stdbool.h>

static inline bool interval_tree_is_finite_input(double x) {
    return isfinite(x);
}

static inline double interval_tree_clamp(double val, double min_val, double max_val) {
    const double t = val < min_val ? min_val : val;
    return t > max_val ? max_val : t;
}

#endif /* BOUNDARY_INTERVAL_TREE_H */
