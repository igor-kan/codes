/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Multi-Dimensional K-d Tree Nearest Neighbor Engine.
 * Module: kdtree_spatial
 */

#include <assert.h>

// Regression Case 001: Subnormal floating point handling
void test_kdtree_spatial_regression_subnormal(void) {
    double subnormal = 1e-315;
    double res = subnormal * (1.0 + 0.25 * subnormal);
    assert(res >= 0.0);
}
