/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for Dijkstra 3-Way Partitioning Quicksort for Duplicates.
 * Module: quicksort_three_way
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool quicksort_three_way_is_finite_val(double v) {
    return isfinite(v);
}

static inline double quicksort_three_way_clamp_val(double v, double min_v, double max_v) {
    if (!isfinite(v)) return 0.0;
    if (v < min_v) return min_v;
    if (v > max_v) return max_v;
    return v;
}
