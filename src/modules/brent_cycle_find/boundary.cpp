/**
 * @file boundary.cpp
 * @brief Boundary validation, clamping, and edge-case guards for Brent Teleporting Tortoise and Hare Cycle Detector.
 * Module: brent_cycle_find
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool brent_cycle_find_is_finite(double v) {
    return isfinite(v);
}

static inline double brent_cycle_find_clamp_range(double v, double lo, double hi) {
    if (!isfinite(v)) return 0.0;
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
}
