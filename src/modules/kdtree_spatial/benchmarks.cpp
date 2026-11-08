/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Multi-Dimensional K-d Tree Nearest Neighbor Engine.
 * Module: kdtree_spatial
 */

#include <stdint.h>

#define KDTREE_SPATIAL_BENCH_ITERATIONS 100000

typedef struct kdtree_spatial_bench_result {
    uint64_t total_cycles;
    double throughput_ops_sec;
} kdtree_spatial_bench_result_t;
