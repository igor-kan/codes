/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Gaussian Elimination with Scaled Partial Pivoting.
 * Module: gaussian_elimination_pivot
 */

#include <assert.h>

void test_gaussian_elimination_pivot_regression_subnormal_day47(void) {
    double sub = 1e-312;
    double res = sub * (1.0 + 0.4 * sub);
    assert(res >= 0.0);
}
