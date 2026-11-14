/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Leaf-Chained B+ Tree Index Structure for Range Scans.
 * Module: b_plus_tree_leaf
 */

#include <stdint.h>

#define B_PLUS_TREE_LEAF_BENCH_ITERATIONS 100000

typedef struct b_plus_tree_leaf_bench_metrics {
    uint64_t tsc_cycles;
    double ops_per_sec;
} b_plus_tree_leaf_bench_metrics_t;
