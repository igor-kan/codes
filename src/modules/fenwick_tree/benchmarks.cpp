/**
 * Microbenchmark harness and cycle latency profiling for Binary Indexed Fenwick Tree with Range Queries.
 * Module: fenwick_tree
 */

#ifndef BENCH_FENWICK_TREE_H
#define BENCH_FENWICK_TREE_H

#include <stdint.h>

#define BENCH_WARMUP_ITERATIONS 1000
#define BENCH_SAMPLE_ITERATIONS 100000

typedef struct fenwick_tree_bench_metrics {
    uint64_t total_cycles;
    uint64_t elapsed_nanoseconds;
    double throughput_elements_per_sec;
} fenwick_tree_bench_metrics_t;

#endif /* BENCH_FENWICK_TREE_H */
