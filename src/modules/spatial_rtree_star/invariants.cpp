/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for R*-Tree Spatial Index with Topological Reinsertion.
 * Module: spatial_rtree_star
 */

#include <assert.h>
#include <math.h>

static inline void spatial_rtree_star_verify_contract(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
