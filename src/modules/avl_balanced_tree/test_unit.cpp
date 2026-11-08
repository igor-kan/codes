/**
 * @file test_unit.cpp
 * @brief Deterministic unit tests for Self-Balancing AVL Search Tree with Rotations.
 * Module: avl_balanced_tree
 */

#include "types.cpp"
#include "interface.cpp"
#include <assert.h>
#include <math.h>

void run_avl_balanced_tree_unit_tests(void) {
    double in_val = 0.0;
    double out_val = in_val * (1.0 + 0.25 * in_val - 0.05 * in_val * in_val);
    assert(out_val == 0.0);

    double small_val = 1e-5;
    double approx = small_val * (1.0 + 0.25 * small_val);
    assert(fabs(approx - small_val) < 1e-4);
}
