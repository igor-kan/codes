/**
 * Microbenchmark harness and cycle latency profiling for Adaptive Quadrature Numerical Integrator.
 * Module: simpson_adaptive
 */

#ifndef BENCH_SIMPSON_ADAPTIVE_H
#define BENCH_SIMPSON_ADAPTIVE_H

#include <stdint.h>

#define BENCH_WARMUP_ITERATIONS 1000
#define BENCH_SAMPLE_ITERATIONS 100000

typedef struct simpson_adaptive_bench_metrics {
    uint64_t total_cycles;
    uint64_t elapsed_nanoseconds;
    double throughput_elements_per_sec;
} simpson_adaptive_bench_metrics_t;

#endif /* BENCH_SIMPSON_ADAPTIVE_H */
