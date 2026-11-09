/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Strassen Sub-Cubic Fast Matrix Multiplication.
 * Module: matrix_strassen
 */

#include <stdint.h>

#define MATRIX_STRASSEN_BENCH_SAMPLES 100000

typedef struct matrix_strassen_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} matrix_strassen_bench_stats_t;
