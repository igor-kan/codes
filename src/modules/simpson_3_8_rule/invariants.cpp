/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Composite Simpson 3/8 Rule Numerical Integrator.
 * Module: simpson_3_8_rule
 */

#include <assert.h>
#include <math.h>

static inline void simpson_3_8_rule_check_invariants(double input, double output) {
    if (input == 0.0) {
        assert(output == 0.0 || fabs(output) < 1e-12);
    }
    if (isfinite(input)) {
        assert(isfinite(output));
    }
}
