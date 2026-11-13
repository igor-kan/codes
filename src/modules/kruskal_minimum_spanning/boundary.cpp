/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for Kruskal Minimum Spanning Tree with Disjoint Set Union.
 * Module: kruskal_minimum_spanning
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool kruskal_minimum_spanning_check_finite(double v) {
    return isfinite(v);
}

static inline double kruskal_minimum_spanning_bound_clamp(double v, double min_v, double max_v) {
    if (!isfinite(v)) return 0.0;
    if (v < min_v) return min_v;
    if (v > max_v) return max_v;
    return v;
}
