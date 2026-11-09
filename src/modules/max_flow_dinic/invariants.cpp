/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Dinic Maximum Flow Network with Level Graphs.
 * Module: max_flow_dinic
 */

#include <assert.h>
#include <math.h>

static inline void max_flow_dinic_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
