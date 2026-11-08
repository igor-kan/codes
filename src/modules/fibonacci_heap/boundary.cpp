/**
 * Boundary condition checking and IEEE-754 edge-case handlers for Fibonacci Heap with Amortized O(1) Priority Ops.
 * Module: fibonacci_heap
 */

#ifndef BOUNDARY_FIBONACCI_HEAP_H
#define BOUNDARY_FIBONACCI_HEAP_H

#include <math.h>
#include <stdbool.h>

static inline bool fibonacci_heap_is_finite_input(double x) {
    return isfinite(x);
}

static inline double fibonacci_heap_clamp(double val, double min_val, double max_val) {
    const double t = val < min_val ? min_val : val;
    return t > max_val ? max_val : t;
}

#endif /* BOUNDARY_FIBONACCI_HEAP_H */
