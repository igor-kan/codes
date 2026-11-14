/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Dijkstra 3-Way Partitioning Quicksort for Duplicates.
 * Module: quicksort_three_way
 */

#include <stdint.h>

#define QUICKSORT_THREE_WAY_BENCH_ITERATIONS 100000

typedef struct quicksort_three_way_bench_metrics {
    uint64_t tsc_cycles;
    double ops_per_sec;
} quicksort_three_way_bench_metrics_t;
