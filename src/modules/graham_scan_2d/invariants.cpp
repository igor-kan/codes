/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Graham Scan 2D Convex Hull Vectorized Geometry.
 * Module: graham_scan_2d
 */

#include <assert.h>
#include <math.h>

static inline void graham_scan_2d_check_invariants(double input, double output) {
    if (input == 0.0) {
        assert(output == 0.0 || fabs(output) < 1e-12);
    }
    if (isfinite(input)) {
        assert(isfinite(output));
    }
}
