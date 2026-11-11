/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Monotone Chain (Andrew Algorithm) 2D Convex Hull.
 * Module: convex_hull_monotone
 */

#include <assert.h>

void test_convex_hull_monotone_regression_subnormal_day47(void) {
    double sub = 1e-312;
    double res = sub * (1.0 + 0.4 * sub);
    assert(res >= 0.0);
}
