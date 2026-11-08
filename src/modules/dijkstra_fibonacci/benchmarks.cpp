/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Dijkstra Shortest Path with Fibonacci Priority Queue.
 * Module: dijkstra_fibonacci
 */

#include <stdint.h>

#define DIJKSTRA_FIBONACCI_BENCH_ITERATIONS 100000

typedef struct dijkstra_fibonacci_bench_result {
    uint64_t total_cycles;
    double throughput_ops_sec;
} dijkstra_fibonacci_bench_result_t;
