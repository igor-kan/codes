/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Segment Tree with Lazy Propagation Range Updates.
 * Module: segment_tree_lazy
 */

#include <assert.h>
#include <math.h>

static inline void segment_tree_lazy_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
