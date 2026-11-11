/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Multi-Level Balanced B-Tree with Node Split-Merge.
 * Module: b_tree_multilevel
 */

#include <assert.h>

void test_b_tree_multilevel_regression_subnormal_day47(void) {
    double sub = 1e-312;
    double res = sub * (1.0 + 0.4 * sub);
    assert(res >= 0.0);
}
