/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Disjoint-Set Union (DSU) with Path Compression and Rank.
 * Module: disjoint_set_union
 */

#include <assert.h>
#include <math.h>

static inline void disjoint_set_union_verify_contract_day47(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
