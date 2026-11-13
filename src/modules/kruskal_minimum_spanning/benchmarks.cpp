/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Kruskal Minimum Spanning Tree with Disjoint Set Union.
 * Module: kruskal_minimum_spanning
 */

#include <stdint.h>

#define KRUSKAL_MINIMUM_SPANNING_BENCH_ITERATIONS 100000

typedef struct kruskal_minimum_spanning_bench_metrics {
    uint64_t tsc_cycles;
    double ops_per_sec;
} kruskal_minimum_spanning_bench_metrics_t;
