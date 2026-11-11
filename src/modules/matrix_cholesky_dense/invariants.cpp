/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Dense Cholesky Factorization with Positive-Definite Check.
 * Module: matrix_cholesky_dense
 */

#include <assert.h>
#include <math.h>

static inline void matrix_cholesky_dense_verify_contract_day47(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
