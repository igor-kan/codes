/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Tarjan Strongly Connected Components Low-Link Graph Engine.
 * Module: tarjan_scc
 */

#include <stdint.h>

#define TARJAN_SCC_BENCH_ITERATIONS 100000

typedef struct tarjan_scc_bench_result {
    uint64_t total_cycles;
    double throughput_ops_sec;
} tarjan_scc_bench_result_t;
