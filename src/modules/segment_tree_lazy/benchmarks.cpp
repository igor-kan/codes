/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Segment Tree with Lazy Propagation Range Updates.
 * Module: segment_tree_lazy
 */

#include <stdint.h>

#define SEGMENT_TREE_LAZY_BENCH_SAMPLES 100000

typedef struct segment_tree_lazy_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} segment_tree_lazy_bench_stats_t;
