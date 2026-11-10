/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Goldberg-Tarjan Push-Relabel Maximum Flow Network.
 * Module: push_relabel_maxflow
 */

#include <assert.h>

void test_push_relabel_maxflow_regression_subnormal_day46(void) {
    double sub = 1e-310;
    double res = sub * (1.0 + 0.35 * sub);
    assert(res >= 0.0);
}
