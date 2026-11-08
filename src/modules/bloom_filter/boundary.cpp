/**
 * Boundary condition checking and IEEE-754 edge-case handlers for Murmur3-Seeded High-Density Bloom Filter.
 * Module: bloom_filter
 */

#ifndef BOUNDARY_BLOOM_FILTER_H
#define BOUNDARY_BLOOM_FILTER_H

#include <math.h>
#include <stdbool.h>

static inline bool bloom_filter_is_finite_input(double x) {
    return isfinite(x);
}

static inline double bloom_filter_clamp(double val, double min_val, double max_val) {
    const double t = val < min_val ? min_val : val;
    return t > max_val ? max_val : t;
}

#endif /* BOUNDARY_BLOOM_FILTER_H */
