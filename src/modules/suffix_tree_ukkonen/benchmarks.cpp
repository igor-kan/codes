/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Ukkonen Linear-Time Online Suffix Tree Construction.
 * Module: suffix_tree_ukkonen
 */

#include <stdint.h>

#define SUFFIX_TREE_UKKONEN_BENCH_SAMPLES 100000

typedef struct suffix_tree_ukkonen_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} suffix_tree_ukkonen_bench_stats_t;
