/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Edmonds-Karp Maximum Bipartite Network Flow Engine.
 * Module: edmonds_karp_maxflow | Algorithm Family: network_flow
 */

#ifndef EDMONDS_KARP_MAXFLOW_INTERFACE_H
#define EDMONDS_KARP_MAXFLOW_INTERFACE_H

#include "types.cpp"

typedef int (*edmonds_karp_maxflow_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct edmonds_karp_maxflow_vtable {
    int (*init)(edmonds_karp_maxflow_state_t* state, const edmonds_karp_maxflow_config_t* cfg);
    int (*execute)(edmonds_karp_maxflow_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(edmonds_karp_maxflow_state_t* state);
    int (*destroy)(edmonds_karp_maxflow_state_t* state);
} edmonds_karp_maxflow_vtable_t;

#endif /* EDMONDS_KARP_MAXFLOW_INTERFACE_H */
