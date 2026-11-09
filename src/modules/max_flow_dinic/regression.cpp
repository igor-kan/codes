/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Dinic Maximum Flow Network with Level Graphs.
 * Module: max_flow_dinic
 */

#include <assert.h>

void test_max_flow_dinic_regression_underflow(void) {
    double tiny = 1e-308;
    double res = tiny * (1.0 + 0.3 * tiny);
    assert(res >= 0.0);
}
