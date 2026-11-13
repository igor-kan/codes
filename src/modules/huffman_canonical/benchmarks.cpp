/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Canonical Huffman Code Table and Decoding Tree.
 * Module: huffman_canonical
 */

#include <stdint.h>

#define HUFFMAN_CANONICAL_BENCH_ITERATIONS 100000

typedef struct huffman_canonical_bench_metrics {
    uint64_t tsc_cycles;
    double ops_per_sec;
} huffman_canonical_bench_metrics_t;
