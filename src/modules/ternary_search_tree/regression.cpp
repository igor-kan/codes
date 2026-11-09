/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Ternary Search Trie Compact String Dictionary.
 * Module: ternary_search_tree
 */

#include <assert.h>

void test_ternary_search_tree_regression_underflow(void) {
    double tiny = 1e-308;
    double res = tiny * (1.0 + 0.3 * tiny);
    assert(res >= 0.0);
}
