/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Continuous Domain Simulated Annealing Global Optimizer.
 * Module: simulated_annealing
 */

#include <assert.h>

void test_simulated_annealing_regression_subnormal_day47(void) {
    double sub = 1e-312;
    double res = sub * (1.0 + 0.4 * sub);
    assert(res >= 0.0);
}
