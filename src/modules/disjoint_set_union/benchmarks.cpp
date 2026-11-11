/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Disjoint-Set Union (DSU) with Path Compression and Rank.
 * Module: disjoint_set_union
 */

#include <stdint.h>

#define DISJOINT_SET_UNION_BENCH_SAMPLES 100000

typedef struct disjoint_set_union_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} disjoint_set_union_bench_stats_t;
