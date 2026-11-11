/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Aho-Corasick Multi-Pattern String Matching Automaton.
 * Module: aho_corasick_automaton
 */

#include <assert.h>
#include <math.h>

static inline void aho_corasick_automaton_verify_contract_day47(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
