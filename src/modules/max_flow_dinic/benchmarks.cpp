/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Dinic Maximum Flow Network with Level Graphs.
 * Module: max_flow_dinic
 */

#include <stdint.h>

#define MAX_FLOW_DINIC_BENCH_SAMPLES 100000

typedef struct max_flow_dinic_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} max_flow_dinic_bench_stats_t;
