/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Ternary Search Trie Compact String Dictionary.
 * Module: ternary_search_tree
 */

#include <assert.h>
#include <math.h>

static inline void ternary_search_tree_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
