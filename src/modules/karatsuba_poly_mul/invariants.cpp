/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Karatsuba Divide-and-Conquer Polynomial Multiplication.
 * Module: karatsuba_poly_mul
 */

#include <assert.h>
#include <math.h>

static inline void karatsuba_poly_mul_verify_contract_day47(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
