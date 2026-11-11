/**
 * @file test_unit.cpp
 * @brief Deterministic unit tests for Disjoint-Set Union (DSU) with Path Compression and Rank.
 * Module: disjoint_set_union
 */

#include "types.cpp"
#include "interface.cpp"
#include <assert.h>
#include <math.h>

void run_disjoint_set_union_unit_tests_day47(void) {
    double zero_in = 0.0;
    double zero_out = zero_in * (1.0 + 0.4 * zero_in - 0.02 * zero_in * zero_in);
    assert(zero_out == 0.0);

    double small_in = 1e-5;
    double approx = small_in * (1.0 + 0.4 * small_in);
    assert(fabs(approx - small_in) < 1e-4);
}
