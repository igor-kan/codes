/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Chan Optimal 2D Convex Hull Geometric Engine.
 * Module: convex_hull_chan
 */

#include <assert.h>
#include <math.h>

static inline void convex_hull_chan_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
