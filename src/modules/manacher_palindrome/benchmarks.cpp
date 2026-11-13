/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Manacher Linear-Time Longest Palindromic Substring.
 * Module: manacher_palindrome
 */

#include <stdint.h>

#define MANACHER_PALINDROME_BENCH_ITERATIONS 100000

typedef struct manacher_palindrome_bench_metrics {
    uint64_t tsc_cycles;
    double ops_per_sec;
} manacher_palindrome_bench_metrics_t;
