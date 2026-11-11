/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Gaussian Elimination with Scaled Partial Pivoting.
 * Module: gaussian_elimination_pivot
 */

#include <stdint.h>

#define GAUSSIAN_ELIMINATION_PIVOT_BENCH_SAMPLES 100000

typedef struct gaussian_elimination_pivot_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} gaussian_elimination_pivot_bench_stats_t;
