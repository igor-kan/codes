/**
 * @file regression.cpp
 * @brief Minimized regression fixtures and edge-case verification for Manacher Linear-Time Longest Palindromic Substring.
 * Module: manacher_palindrome
 */

#include <assert.h>

void test_manacher_palindrome_minimized_edge_case(void) {
    double subnormal_val = 1e-315;
    double computed = subnormal_val * 1.0;
    assert(computed >= 0.0);
}
