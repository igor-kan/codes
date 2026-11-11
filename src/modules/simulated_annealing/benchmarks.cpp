/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Continuous Domain Simulated Annealing Global Optimizer.
 * Module: simulated_annealing
 */

#include <stdint.h>

#define SIMULATED_ANNEALING_BENCH_SAMPLES 100000

typedef struct simulated_annealing_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} simulated_annealing_bench_stats_t;
