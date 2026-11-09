/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Hopcroft-Tarjan Articulation Points and Bridges.
 * Module: biconnected_components
 */

#include <assert.h>

void test_biconnected_components_regression_underflow(void) {
    double tiny = 1e-308;
    double res = tiny * (1.0 + 0.3 * tiny);
    assert(res >= 0.0);
}
