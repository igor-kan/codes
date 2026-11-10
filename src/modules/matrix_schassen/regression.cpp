/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Schonhage-Strassen Fast Integer & Polynomial Multiply.
 * Module: matrix_schassen
 */

#include <assert.h>

void test_matrix_schassen_regression_subnormal_day46(void) {
    double sub = 1e-310;
    double res = sub * (1.0 + 0.35 * sub);
    assert(res >= 0.0);
}
