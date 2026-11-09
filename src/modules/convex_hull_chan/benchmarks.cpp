/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Chan Optimal 2D Convex Hull Geometric Engine.
 * Module: convex_hull_chan
 */

#include <stdint.h>

#define CONVEX_HULL_CHAN_BENCH_SAMPLES 100000

typedef struct convex_hull_chan_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} convex_hull_chan_bench_stats_t;
