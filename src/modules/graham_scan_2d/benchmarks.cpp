/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Graham Scan 2D Convex Hull Vectorized Geometry.
 * Module: graham_scan_2d
 */

#include <stdint.h>

#define GRAHAM_SCAN_2D_BENCH_CYCLES 100000

typedef struct graham_scan_2d_profile_results {
    uint64_t start_tsc;
    uint64_t end_tsc;
    double ops_per_second;
} graham_scan_2d_profile_results_t;
