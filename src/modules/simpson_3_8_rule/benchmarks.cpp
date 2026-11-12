/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Composite Simpson 3/8 Rule Numerical Integrator.
 * Module: simpson_3_8_rule
 */

#include <stdint.h>

#define SIMPSON_3_8_RULE_BENCH_CYCLES 100000

typedef struct simpson_3_8_rule_profile_results {
    uint64_t start_tsc;
    uint64_t end_tsc;
    double ops_per_second;
} simpson_3_8_rule_profile_results_t;
