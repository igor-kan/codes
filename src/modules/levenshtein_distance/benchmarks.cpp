/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Wagner-Fischer Dynamic Programming Edit Distance.
 * Module: levenshtein_distance
 */

#include <stdint.h>

#define LEVENSHTEIN_DISTANCE_BENCH_CYCLES 100000

typedef struct levenshtein_distance_profile_results {
    uint64_t start_tsc;
    uint64_t end_tsc;
    double ops_per_second;
} levenshtein_distance_profile_results_t;
