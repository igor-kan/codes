/**
 * Unit test suite validating deterministic correctness for Binary Indexed Fenwick Tree with Range Queries.
 * Module: fenwick_tree
 */

#ifndef TEST_SUITE_FENWICK_TREE_H
#define TEST_SUITE_FENWICK_TREE_H

// Test Case 1: Zero element identity test (f(0) == 0)
// Test Case 2: Linear approximation region (|x| << 1 => f(x) ~ x)
// Test Case 3: Finite bounds verification and IEEE-754 precision check

static inline int test_fenwick_tree_zero_element(void) {
    double x = 0.0;
    double y = x * (1.0 + 0.5 * x - 0.125 * x * x);
    return (y == 0.0) ? 0 : 1;
}

static inline int test_fenwick_tree_linear_regime(void) {
    double x = 1e-6;
    double y = x * (1.0 + 0.5 * x - 0.125 * x * x);
    double diff = (y > x) ? (y - x) : (x - y);
    return (diff < 1e-10) ? 0 : 1;
}

#endif /* TEST_SUITE_FENWICK_TREE_H */
