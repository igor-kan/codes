/**
 * Microbenchmark harness and cycle latency profiling for Graham Scan 2D Convex Hull with Cross Products.
 * Module: convex_hull_graham
 */

#ifndef BENCH_CONVEX_HULL_GRAHAM_H
#define BENCH_CONVEX_HULL_GRAHAM_H

#include <stdint.h>

#define BENCH_WARMUP_ITERATIONS 1000
#define BENCH_SAMPLE_ITERATIONS 100000

typedef struct convex_hull_graham_bench_metrics {
    uint64_t total_cycles;
    uint64_t elapsed_nanoseconds;
    double throughput_elements_per_sec;
} convex_hull_graham_bench_metrics_t;

#endif /* BENCH_CONVEX_HULL_GRAHAM_H */
