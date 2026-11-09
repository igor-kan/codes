/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Ternary Search Trie Compact String Dictionary.
 * Module: ternary_search_tree
 */

#include <stdint.h>

#define TERNARY_SEARCH_TREE_BENCH_SAMPLES 100000

typedef struct ternary_search_tree_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} ternary_search_tree_bench_stats_t;
