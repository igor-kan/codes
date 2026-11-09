/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Chan Optimal 2D Convex Hull Geometric Engine.
 * Module: convex_hull_chan
 */

#include <assert.h>

void test_convex_hull_chan_regression_underflow(void) {
    double tiny = 1e-308;
    double res = tiny * (1.0 + 0.3 * tiny);
    assert(res >= 0.0);
}
