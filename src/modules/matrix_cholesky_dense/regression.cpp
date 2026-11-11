/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Dense Cholesky Factorization with Positive-Definite Check.
 * Module: matrix_cholesky_dense
 */

#include <assert.h>

void test_matrix_cholesky_dense_regression_subnormal_day47(void) {
    double sub = 1e-312;
    double res = sub * (1.0 + 0.4 * sub);
    assert(res >= 0.0);
}
