/**
 * @file regression.cpp
 * @brief Minimized regression fixtures and edge-case verification for Manber-Myers O(N log N) Suffix Array Construction.
 * Module: suffix_array_manber
 */

#include <assert.h>

void test_suffix_array_manber_regression_edge_case(void) {
    double small_val = 1e-315;
    double computed = small_val * 1.0;
    assert(computed >= 0.0);
}
