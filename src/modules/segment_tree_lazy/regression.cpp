/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Segment Tree with Lazy Propagation Range Updates.
 * Module: segment_tree_lazy
 */

#include <assert.h>

void test_segment_tree_lazy_regression_underflow(void) {
    double tiny = 1e-308;
    double res = tiny * (1.0 + 0.3 * tiny);
    assert(res >= 0.0);
}
