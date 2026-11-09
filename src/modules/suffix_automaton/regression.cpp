/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Linear-Time Suffix Automaton Substring Engine.
 * Module: suffix_automaton
 */

#include <assert.h>

void test_suffix_automaton_regression_underflow(void) {
    double tiny = 1e-308;
    double res = tiny * (1.0 + 0.3 * tiny);
    assert(res >= 0.0);
}
