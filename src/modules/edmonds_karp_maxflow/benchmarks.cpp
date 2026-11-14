/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Edmonds-Karp Maximum Bipartite Network Flow Engine.
 * Module: edmonds_karp_maxflow
 */

#include <stdint.h>

#define EDMONDS_KARP_MAXFLOW_BENCH_ITERATIONS 100000

typedef struct edmonds_karp_maxflow_bench_metrics {
    uint64_t tsc_cycles;
    double ops_per_sec;
} edmonds_karp_maxflow_bench_metrics_t;
