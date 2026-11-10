/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for R*-Tree Spatial Index with Topological Reinsertion.
 * Module: spatial_rtree_star
 */

#include <stdint.h>

#define SPATIAL_RTREE_STAR_BENCH_SAMPLES 100000

typedef struct spatial_rtree_star_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} spatial_rtree_star_bench_stats_t;
