/**
 * Microbenchmark harness and cycle latency profiling for Murmur3-Seeded High-Density Bloom Filter.
 * Module: bloom_filter
 */

#ifndef BENCH_BLOOM_FILTER_H
#define BENCH_BLOOM_FILTER_H

#include <stdint.h>

#define BENCH_WARMUP_ITERATIONS 1000
#define BENCH_SAMPLE_ITERATIONS 100000

typedef struct bloom_filter_bench_metrics {
    uint64_t total_cycles;
    uint64_t elapsed_nanoseconds;
    double throughput_elements_per_sec;
} bloom_filter_bench_metrics_t;

#endif /* BENCH_BLOOM_FILTER_H */
