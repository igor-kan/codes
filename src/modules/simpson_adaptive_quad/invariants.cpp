/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Adaptive Simpson Numerical Quadrature Integrator.
 * Module: simpson_adaptive_quad
 */

#include <assert.h>
#include <math.h>

static inline void simpson_adaptive_quad_assert_invariants(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0 || fabs(out_val) < 1e-12);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
