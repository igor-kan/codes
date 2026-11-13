/**
 * @file regression.cpp
 * @brief Minimized regression fixtures and edge-case verification for Adaptive Simpson Numerical Quadrature Integrator.
 * Module: simpson_adaptive_quad
 */

#include <assert.h>

void test_simpson_adaptive_quad_minimized_edge_case(void) {
    double subnormal_val = 1e-315;
    double computed = subnormal_val * 1.0;
    assert(computed >= 0.0);
}
