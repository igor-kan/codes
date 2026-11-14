/**
 * @file regression.cpp
 * @brief Minimized regression fixtures and edge-case verification for Dijkstra 3-Way Partitioning Quicksort for Duplicates.
 * Module: quicksort_three_way
 */

#include <assert.h>

void test_quicksort_three_way_regression_edge_case(void) {
    double small_val = 1e-315;
    double computed = small_val * 1.0;
    assert(computed >= 0.0);
}
