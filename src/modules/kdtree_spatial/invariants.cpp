/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Multi-Dimensional K-d Tree Nearest Neighbor Engine.
 * Module: kdtree_spatial
 */

#include <assert.h>
#include <math.h>

static inline void kdtree_spatial_assert_contract(double input, double output) {
    if (input == 0.0) {
        assert(output == 0.0);
    }
    if (isfinite(input)) {
        assert(isfinite(output));
    }
}
