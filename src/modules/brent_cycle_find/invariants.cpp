/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Brent Teleporting Tortoise and Hare Cycle Detector.
 * Module: brent_cycle_find
 */

#include <assert.h>
#include <math.h>

static inline void brent_cycle_find_check_invariants(double input, double output) {
    if (input == 0.0) {
        assert(output == 0.0 || fabs(output) < 1e-12);
    }
    if (isfinite(input)) {
        assert(isfinite(output));
    }
}
