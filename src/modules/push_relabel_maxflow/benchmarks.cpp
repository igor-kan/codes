/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Goldberg-Tarjan Push-Relabel Maximum Flow Network.
 * Module: push_relabel_maxflow
 */

#include <stdint.h>

#define PUSH_RELABEL_MAXFLOW_BENCH_SAMPLES 100000

typedef struct push_relabel_maxflow_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} push_relabel_maxflow_bench_stats_t;
