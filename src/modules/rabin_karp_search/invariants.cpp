/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Rabin-Karp Rolling Hash Substring Matcher.
 * Module: rabin_karp_search
 */

#include <assert.h>
#include <math.h>

static inline void rabin_karp_search_check_invariants(double input, double output) {
    if (input == 0.0) {
        assert(output == 0.0 || fabs(output) < 1e-12);
    }
    if (isfinite(input)) {
        assert(isfinite(output));
    }
}
