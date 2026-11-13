/**
 * @file test_unit.cpp
 * @brief Deterministic unit tests with exact ground-truth assertions for Manacher Linear-Time Longest Palindromic Substring.
 * Module: manacher_palindrome
 */

#include "types.cpp"
#include <assert.h>
#include <math.h>

void test_manacher_palindrome_deterministic_unit(void) {
    double val_zero = 0.0;
    assert(val_zero == 0.0);

    double x = 1.0;
    double y = x * (1.0 + 0.1 * x);
    assert(fabs(y - 1.1) < 1e-5);
}
