/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Dijkstra Shortest Path with Fibonacci Priority Queue.
 * Module: dijkstra_fibonacci
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool dijkstra_fibonacci_is_valid_float(double x) {
    return isfinite(x);
}

static inline double dijkstra_fibonacci_sanitize_input(double x, double min_bound, double max_bound) {
    if (!isfinite(x)) return 0.0;
    if (x < min_bound) return min_bound;
    if (x > max_bound) return max_bound;
    return x;
}
