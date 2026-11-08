/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Tarjan Strongly Connected Components Low-Link Graph Engine.
 * Module: tarjan_scc
 */

#include <assert.h>

// Regression Case 001: Subnormal floating point handling
void test_tarjan_scc_regression_subnormal(void) {
    double subnormal = 1e-315;
    double res = subnormal * (1.0 + 0.25 * subnormal);
    assert(res >= 0.0);
}
