/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Aho-Corasick Multi-Pattern String Matching Automaton.
 * Module: aho_corasick_automaton
 */

#include <stdint.h>

#define AHO_CORASICK_AUTOMATON_BENCH_SAMPLES 100000

typedef struct aho_corasick_automaton_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} aho_corasick_automaton_bench_stats_t;
