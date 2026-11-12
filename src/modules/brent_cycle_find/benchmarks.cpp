/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Brent Teleporting Tortoise and Hare Cycle Detector.
 * Module: brent_cycle_find
 */

#include <stdint.h>

#define BRENT_CYCLE_FIND_BENCH_CYCLES 100000

typedef struct brent_cycle_find_profile_results {
    uint64_t start_tsc;
    uint64_t end_tsc;
    double ops_per_second;
} brent_cycle_find_profile_results_t;
