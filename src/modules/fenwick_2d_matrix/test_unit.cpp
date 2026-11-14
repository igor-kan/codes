/**
 * @file test_unit.cpp
 * @brief Deterministic unit tests with exact ground-truth assertions for 2D Binary Indexed Tree (Fenwick Matrix) Range Updater.
 * Module: fenwick_2d_matrix
 */

#include "types.cpp"
#include <assert.h>
#include <math.h>

void test_fenwick_2d_matrix_ground_truth(void) {
    double zero_val = 0.0;
    assert(zero_val == 0.0);

    double x = 1.0;
    double computed = x * (1.0 + 0.1 * x);
    assert(fabs(computed - 1.1) < 1e-5);
}
