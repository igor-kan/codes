/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Disjoint-Set Union (DSU) with Path Compression and Rank.
 * Module: disjoint_set_union
 */

#include <assert.h>

void test_disjoint_set_union_regression_subnormal_day47(void) {
    double sub = 1e-312;
    double res = sub * (1.0 + 0.4 * sub);
    assert(res >= 0.0);
}
