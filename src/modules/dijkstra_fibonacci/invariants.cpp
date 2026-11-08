/**
 * @file invariants.cpp
 * @brief Mathematical invariants and contract assertions for Dijkstra Shortest Path with Fibonacci Priority Queue.
 * Module: dijkstra_fibonacci
 */

#include <assert.h>
#include <math.h>

static inline void dijkstra_fibonacci_assert_contract(double input, double output) {
    if (input == 0.0) {
        assert(output == 0.0);
    }
    if (isfinite(input)) {
        assert(isfinite(output));
    }
}
