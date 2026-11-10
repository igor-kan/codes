/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Schonhage-Strassen Fast Integer & Polynomial Multiply.
 * Module: matrix_schassen
 */

#include <assert.h>
#include <math.h>

static inline void matrix_schassen_verify_contract(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
