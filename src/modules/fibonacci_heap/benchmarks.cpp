/**
 * Microbenchmark harness and cycle latency profiling for Fibonacci Heap with Amortized O(1) Priority Ops.
 * Module: fibonacci_heap
 */

#ifndef BENCH_FIBONACCI_HEAP_H
#define BENCH_FIBONACCI_HEAP_H

#include <stdint.h>

#define BENCH_WARMUP_ITERATIONS 1000
#define BENCH_SAMPLE_ITERATIONS 100000

typedef struct fibonacci_heap_bench_metrics {
    uint64_t total_cycles;
    uint64_t elapsed_nanoseconds;
    double throughput_elements_per_sec;
} fibonacci_heap_bench_metrics_t;

#endif /* BENCH_FIBONACCI_HEAP_H */
