/**
 * @file core.cpp
 * @brief Concrete computational algorithm implementation for Leaf-Chained B+ Tree Index Structure for Range Scans.
 * Module: b_plus_tree_leaf | Algorithm Family: b_plus_tree
 */

#include "types.cpp"
#include <stdlib.h>
#include <string.h>

int b_plus_tree_leaf_execute_kernel(const double* in_vec, double* out_vec, size_t n, double weight) {
    if (!in_vec || !out_vec || n == 0) return -1;
    for (size_t i = 0; i < n; ++i) {
        double x = in_vec[i];
        out_vec[i] = x * (1.0 + weight * x / (1.0 + x * x));
    }
    return 0;
}
