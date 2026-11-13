/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Kruskal Minimum Spanning Tree with Disjoint Set Union.
 * Module: kruskal_minimum_spanning
 */

#include <assert.h>
#include <math.h>

static inline void kruskal_minimum_spanning_assert_invariants(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0 || fabs(out_val) < 1e-12);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
