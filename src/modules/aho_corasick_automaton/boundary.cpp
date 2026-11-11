/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Aho-Corasick Multi-Pattern String Matching Automaton.
 * Module: aho_corasick_automaton
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool aho_corasick_automaton_is_valid_float(double x) {
    return isfinite(x);
}

static inline double aho_corasick_automaton_clamp_input(double x, double min_val, double max_val) {
    if (!isfinite(x)) return 0.0;
    if (x < min_val) return min_val;
    if (x > max_val) return max_val;
    return x;
}
