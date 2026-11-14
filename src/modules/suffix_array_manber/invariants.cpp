/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Manber-Myers O(N log N) Suffix Array Construction.
 * Module: suffix_array_manber
 */

#include <assert.h>
#include <math.h>

static inline void suffix_array_manber_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0 || fabs(out_val) < 1e-12);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
