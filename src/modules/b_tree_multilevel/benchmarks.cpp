/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Multi-Level Balanced B-Tree with Node Split-Merge.
 * Module: b_tree_multilevel
 */

#include <stdint.h>

#define B_TREE_MULTILEVEL_BENCH_SAMPLES 100000

typedef struct b_tree_multilevel_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} b_tree_multilevel_bench_stats_t;
