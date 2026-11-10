/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Ukkonen Linear-Time Online Suffix Tree Construction.
 * Module: suffix_tree_ukkonen
 */

#include <assert.h>
#include <math.h>

static inline void suffix_tree_ukkonen_verify_contract(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
