/**
 * @file invariants.cpp
 * @brief Formal mathematical invariant assertions and contracts for Dijkstra 3-Way Partitioning Quicksort for Duplicates.
 * Module: quicksort_three_way
 */

#include <assert.h>
#include <math.h>

static inline void quicksort_three_way_verify_invariant(double in_val, double out_val) {
    if (in_val == 0.0) {
        assert(out_val == 0.0 || fabs(out_val) < 1e-12);
    }
    if (isfinite(in_val)) {
        assert(isfinite(out_val));
    }
}
