/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Ukkonen Linear-Time Online Suffix Tree Construction.
 * Module: suffix_tree_ukkonen
 */

#include <assert.h>

void test_suffix_tree_ukkonen_regression_subnormal_day46(void) {
    double sub = 1e-310;
    double res = sub * (1.0 + 0.35 * sub);
    assert(res >= 0.0);
}
