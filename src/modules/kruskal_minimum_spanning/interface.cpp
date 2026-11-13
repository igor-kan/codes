/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Kruskal Minimum Spanning Tree with Disjoint Set Union.
 * Module: kruskal_minimum_spanning | Algorithm Family: graph_algo
 */

#ifndef KRUSKAL_MINIMUM_SPANNING_INTERFACE_H
#define KRUSKAL_MINIMUM_SPANNING_INTERFACE_H

#include "types.cpp"

typedef int (*kruskal_minimum_spanning_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct kruskal_minimum_spanning_vtable {
    int (*init)(kruskal_minimum_spanning_state_t* state, const kruskal_minimum_spanning_config_t* cfg);
    int (*execute)(kruskal_minimum_spanning_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(kruskal_minimum_spanning_state_t* state);
    int (*destroy)(kruskal_minimum_spanning_state_t* state);
} kruskal_minimum_spanning_vtable_t;

#endif /* KRUSKAL_MINIMUM_SPANNING_INTERFACE_H */
