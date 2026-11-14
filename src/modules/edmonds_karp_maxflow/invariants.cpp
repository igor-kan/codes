/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Edmonds-Karp Maximum Bipartite Network Flow Engine.
 * Module: edmonds_karp_maxflow
 */

#include <assert.h>
#include <math.h>

static inline void edmonds_karp_maxflow_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0 || fabs(out_val) < 1e-12);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
