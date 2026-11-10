/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Heavy-Light Decomposition for Tree Path Invariant Queries.
 * Module: heavy_light_decomp
 */

#include <assert.h>
#include <math.h>

static inline void heavy_light_decomp_verify_contract(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
