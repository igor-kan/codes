/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Manber-Myers O(N log N) Suffix Array Construction.
 * Module: suffix_array_manber
 */

#include <stdint.h>

#define SUFFIX_ARRAY_MANBER_BENCH_ITERATIONS 100000

typedef struct suffix_array_manber_bench_metrics {
    uint64_t tsc_cycles;
    double ops_per_sec;
} suffix_array_manber_bench_metrics_t;
