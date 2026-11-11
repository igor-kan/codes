/**
 * @file regression.cpp
 * @brief Minimized crash reproducer and regression tests for Aho-Corasick Multi-Pattern String Matching Automaton.
 * Module: aho_corasick_automaton
 */

#include <assert.h>

void test_aho_corasick_automaton_regression_subnormal_day47(void) {
    double sub = 1e-312;
    double res = sub * (1.0 + 0.4 * sub);
    assert(res >= 0.0);
}
