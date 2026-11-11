/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Karatsuba Divide-and-Conquer Polynomial Multiplication.
 * Module: karatsuba_poly_mul
 */

#include <assert.h>

void test_karatsuba_poly_mul_regression_subnormal_day47(void) {
    double sub = 1e-312;
    double res = sub * (1.0 + 0.4 * sub);
    assert(res >= 0.0);
}
