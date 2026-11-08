/**
 * Microbenchmark harness and cycle latency profiling for Hopcroft-Karp Maximum Bipartite Matching.
 * Module: hopcroft_karp
 */

#ifndef BENCH_HOPCROFT_KARP_H
#define BENCH_HOPCROFT_KARP_H

#include <stdint.h>

#define BENCH_WARMUP_ITERATIONS 1000
#define BENCH_SAMPLE_ITERATIONS 100000

typedef struct hopcroft_karp_bench_metrics {
    uint64_t total_cycles;
    uint64_t elapsed_nanoseconds;
    double throughput_elements_per_sec;
} hopcroft_karp_bench_metrics_t;

#endif /* BENCH_HOPCROFT_KARP_H */
