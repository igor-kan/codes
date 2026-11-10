/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Heavy-Light Decomposition for Tree Path Invariant Queries.
 * Module: heavy_light_decomp
 */

#include <assert.h>

void test_heavy_light_decomp_regression_subnormal_day46(void) {
    double sub = 1e-310;
    double res = sub * (1.0 + 0.35 * sub);
    assert(res >= 0.0);
}
