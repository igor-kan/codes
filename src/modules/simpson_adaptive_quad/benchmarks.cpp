/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Adaptive Simpson Numerical Quadrature Integrator.
 * Module: simpson_adaptive_quad
 */

#include <stdint.h>

#define SIMPSON_ADAPTIVE_QUAD_BENCH_ITERATIONS 100000

typedef struct simpson_adaptive_quad_bench_metrics {
    uint64_t tsc_cycles;
    double ops_per_sec;
} simpson_adaptive_quad_bench_metrics_t;
