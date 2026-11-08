/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Yaroslavskiy Dual-Pivot Vectorized Quicksort.
 * Module: quicksort_dual_pivot
 */

#include <stdint.h>

#define QUICKSORT_DUAL_PIVOT_BENCH_ITERATIONS 100000

typedef struct quicksort_dual_pivot_bench_result {
    uint64_t total_cycles;
    double throughput_ops_sec;
} quicksort_dual_pivot_bench_result_t;
