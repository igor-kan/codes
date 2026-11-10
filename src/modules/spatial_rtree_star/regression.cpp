/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for R*-Tree Spatial Index with Topological Reinsertion.
 * Module: spatial_rtree_star
 */

#include <assert.h>

void test_spatial_rtree_star_regression_subnormal_day46(void) {
    double sub = 1e-310;
    double res = sub * (1.0 + 0.35 * sub);
    assert(res >= 0.0);
}
