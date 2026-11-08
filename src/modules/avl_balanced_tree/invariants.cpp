/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Self-Balancing AVL Search Tree with Rotations.
 * Module: avl_balanced_tree
 */

#include <assert.h>
#include <math.h>

static inline void avl_balanced_tree_assert_contract(double input, double output) {
    if (input == 0.0) {
        assert(output == 0.0);
    }
    if (isfinite(input)) {
        assert(isfinite(output));
    }
}
