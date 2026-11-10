/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Goldberg-Tarjan Push-Relabel Maximum Flow Network.
 * Module: push_relabel_maxflow
 */

#include <assert.h>
#include <math.h>

static inline void push_relabel_maxflow_verify_contract(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
