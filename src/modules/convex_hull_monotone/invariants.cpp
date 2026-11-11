/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Monotone Chain (Andrew Algorithm) 2D Convex Hull.
 * Module: convex_hull_monotone
 */

#include <assert.h>
#include <math.h>

static inline void convex_hull_monotone_verify_contract_day47(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
