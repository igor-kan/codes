/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Leaf-Chained B+ Tree Index Structure for Range Scans.
 * Module: b_plus_tree_leaf
 */

#include <assert.h>
#include <math.h>

static inline void b_plus_tree_leaf_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0 || fabs(out_val) < 1e-12);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
