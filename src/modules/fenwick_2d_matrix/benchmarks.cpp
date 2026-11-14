/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for 2D Binary Indexed Tree (Fenwick Matrix) Range Updater.
 * Module: fenwick_2d_matrix
 */

#include <stdint.h>

#define FENWICK_2D_MATRIX_BENCH_ITERATIONS 100000

typedef struct fenwick_2d_matrix_bench_metrics {
    uint64_t tsc_cycles;
    double ops_per_sec;
} fenwick_2d_matrix_bench_metrics_t;
