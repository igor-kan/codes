/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and latency profiling for Canonical Huffman Variable-Length Entropy Codec.
 * Module: huffman_codec
 */

#include <stdint.h>

#define HUFFMAN_CODEC_BENCH_CYCLES 100000

typedef struct huffman_codec_profile_results {
    uint64_t start_tsc;
    uint64_t end_tsc;
    double ops_per_second;
} huffman_codec_profile_results_t;
