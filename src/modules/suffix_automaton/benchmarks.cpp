/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Linear-Time Suffix Automaton Substring Engine.
 * Module: suffix_automaton
 */

#include <stdint.h>

#define SUFFIX_AUTOMATON_BENCH_SAMPLES 100000

typedef struct suffix_automaton_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} suffix_automaton_bench_stats_t;
