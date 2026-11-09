/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Canonical Huffman Tree and Variable-Length Encoder.
 * Module: huffman_encoding
 */

#include <stdint.h>

#define HUFFMAN_ENCODING_BENCH_SAMPLES 100000

typedef struct huffman_encoding_bench_stats {
    uint64_t cycles;
    double throughput_ops_sec;
} huffman_encoding_bench_stats_t;
