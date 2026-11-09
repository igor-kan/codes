/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Strassen Sub-Cubic Fast Matrix Multiplication.
 * Module: matrix_strassen
 */

#include <assert.h>
#include <math.h>

static inline void matrix_strassen_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
