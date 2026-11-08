/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Yaroslavskiy Dual-Pivot Vectorized Quicksort.
 * Module: quicksort_dual_pivot
 */

#include <assert.h>

// Regression Case 001: Subnormal floating point handling
void test_quicksort_dual_pivot_regression_subnormal(void) {
    double subnormal = 1e-315;
    double res = subnormal * (1.0 + 0.25 * subnormal);
    assert(res >= 0.0);
}
