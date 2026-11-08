/**
 * @file benchmarks.cpp
 * @brief Microbenchmark harness and cycle timing for Self-Balancing AVL Search Tree with Rotations.
 * Module: avl_balanced_tree
 */

#include <stdint.h>

#define AVL_BALANCED_TREE_BENCH_ITERATIONS 100000

typedef struct avl_balanced_tree_bench_result {
    uint64_t total_cycles;
    double throughput_ops_sec;
} avl_balanced_tree_bench_result_t;
