/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Monotone Chain (Andrew Algorithm) 2D Convex Hull.
 * Module: convex_hull_monotone
 */

#include <stdint.h>

#define CONVEX_HULL_MONOTONE_BENCH_SAMPLES 100000

typedef struct convex_hull_monotone_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} convex_hull_monotone_bench_stats_t;
