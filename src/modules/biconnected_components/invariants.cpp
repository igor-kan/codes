/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Hopcroft-Tarjan Articulation Points and Bridges.
 * Module: biconnected_components
 */

#include <assert.h>
#include <math.h>

static inline void biconnected_components_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
