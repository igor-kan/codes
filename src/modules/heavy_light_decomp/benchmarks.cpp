/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Heavy-Light Decomposition for Tree Path Invariant Queries.
 * Module: heavy_light_decomp
 */

#include <stdint.h>

#define HEAVY_LIGHT_DECOMP_BENCH_SAMPLES 100000

typedef struct heavy_light_decomp_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} heavy_light_decomp_bench_stats_t;
