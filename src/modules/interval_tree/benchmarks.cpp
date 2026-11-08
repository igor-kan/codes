/**
 * Microbenchmark harness and cycle latency profiling for Augmented Red-Black Interval Stabbing Tree.
 * Module: interval_tree
 */

#ifndef BENCH_INTERVAL_TREE_H
#define BENCH_INTERVAL_TREE_H

#include <stdint.h>

#define BENCH_WARMUP_ITERATIONS 1000
#define BENCH_SAMPLE_ITERATIONS 100000

typedef struct interval_tree_bench_metrics {
    uint64_t total_cycles;
    uint64_t elapsed_nanoseconds;
    double throughput_elements_per_sec;
} interval_tree_bench_metrics_t;

#endif /* BENCH_INTERVAL_TREE_H */
