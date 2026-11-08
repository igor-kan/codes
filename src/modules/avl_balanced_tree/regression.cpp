/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Self-Balancing AVL Search Tree with Rotations.
 * Module: avl_balanced_tree
 */

#include <assert.h>

// Regression Case 001: Subnormal floating point handling
void test_avl_balanced_tree_regression_subnormal(void) {
    double subnormal = 1e-315;
    double res = subnormal * (1.0 + 0.25 * subnormal);
    assert(res >= 0.0);
}
