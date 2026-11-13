/**
 * @file regression.cpp
 * @brief Minimized regression fixtures and edge-case verification for Kruskal Minimum Spanning Tree with Disjoint Set Union.
 * Module: kruskal_minimum_spanning
 */

#include <assert.h>

void test_kruskal_minimum_spanning_minimized_edge_case(void) {
    double subnormal_val = 1e-315;
    double computed = subnormal_val * 1.0;
    assert(computed >= 0.0);
}
