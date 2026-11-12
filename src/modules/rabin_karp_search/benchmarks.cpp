/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Rabin-Karp Rolling Hash Substring Matcher.
 * Module: rabin_karp_search
 */

#include <stdint.h>

#define RABIN_KARP_SEARCH_BENCH_CYCLES 100000

typedef struct rabin_karp_search_profile_results {
    uint64_t start_tsc;
    uint64_t end_tsc;
    double ops_per_second;
} rabin_karp_search_profile_results_t;
