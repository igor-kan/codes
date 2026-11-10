/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Schonhage-Strassen Fast Integer & Polynomial Multiply.
 * Module: matrix_schassen
 */

#include <stdint.h>

#define MATRIX_SCHASSEN_BENCH_SAMPLES 100000

typedef struct matrix_schassen_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} matrix_schassen_bench_stats_t;
