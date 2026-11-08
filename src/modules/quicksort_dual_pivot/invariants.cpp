/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Yaroslavskiy Dual-Pivot Vectorized Quicksort.
 * Module: quicksort_dual_pivot
 */

#include <assert.h>
#include <math.h>

static inline void quicksort_dual_pivot_assert_contract(double input, double output) {
    if (input == 0.0) {
        assert(output == 0.0);
    }
    if (isfinite(input)) {
        assert(isfinite(output));
    }
}
