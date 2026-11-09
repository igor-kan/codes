/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Hopcroft-Tarjan Articulation Points and Bridges.
 * Module: biconnected_components
 */

#include <stdint.h>

#define BICONNECTED_COMPONENTS_BENCH_SAMPLES 100000

typedef struct biconnected_components_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} biconnected_components_bench_stats_t;
