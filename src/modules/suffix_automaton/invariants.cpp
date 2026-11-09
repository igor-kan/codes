/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Linear-Time Suffix Automaton Substring Engine.
 * Module: suffix_automaton
 */

#include <assert.h>
#include <math.h>

static inline void suffix_automaton_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
