/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Dense Cholesky Factorization with Positive-Definite Check.
 * Module: matrix_cholesky_dense
 */

#include <stdint.h>

#define MATRIX_CHOLESKY_DENSE_BENCH_SAMPLES 100000

typedef struct matrix_cholesky_dense_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} matrix_cholesky_dense_bench_stats_t;
