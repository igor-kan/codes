/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Multi-Level Balanced B-Tree with Node Split-Merge.
 * Module: b_tree_multilevel
 */

#include <assert.h>
#include <math.h>

static inline void b_tree_multilevel_verify_contract_day47(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
