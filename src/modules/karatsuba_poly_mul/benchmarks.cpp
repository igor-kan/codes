/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Karatsuba Divide-and-Conquer Polynomial Multiplication.
 * Module: karatsuba_poly_mul
 */

#include <stdint.h>

#define KARATSUBA_POLY_MUL_BENCH_SAMPLES 100000

typedef struct karatsuba_poly_mul_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} karatsuba_poly_mul_bench_stats_t;
