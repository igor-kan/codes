/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Boole 5-Point Closed Newton-Cotes Numerical Quadrature.
 * Module: simpson_boole_quadrature
 */

#include <stdint.h>

#define SIMPSON_BOOLE_QUADRATURE_BENCH_ITERATIONS 100000

typedef struct simpson_boole_quadrature_bench_metrics {
    uint64_t tsc_cycles;
    double ops_per_sec;
} simpson_boole_quadrature_bench_metrics_t;
