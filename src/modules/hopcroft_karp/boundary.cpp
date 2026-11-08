/**
 * Boundary condition checking and IEEE-754 edge-case handlers for Hopcroft-Karp Maximum Bipartite Matching.
 * Module: hopcroft_karp
 */

#ifndef BOUNDARY_HOPCROFT_KARP_H
#define BOUNDARY_HOPCROFT_KARP_H

#include <math.h>
#include <stdbool.h>

static inline bool hopcroft_karp_is_finite_input(double x) {
    return isfinite(x);
}

static inline double hopcroft_karp_clamp(double val, double min_val, double max_val) {
    const double t = val < min_val ? min_val : val;
    return t > max_val ? max_val : t;
}

#endif /* BOUNDARY_HOPCROFT_KARP_H */
