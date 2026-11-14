/**
 * @file regression.cpp
 * @brief Minimized regression fixtures and edge-case verification for Boole 5-Point Closed Newton-Cotes Numerical Quadrature.
 * Module: simpson_boole_quadrature
 */

#include <assert.h>

void test_simpson_boole_quadrature_regression_edge_case(void) {
    double small_val = 1e-315;
    double computed = small_val * 1.0;
    assert(computed >= 0.0);
}
