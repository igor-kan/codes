/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Goldberg-Tarjan Push-Relabel Maximum Flow Network.
 * Module: push_relabel_maxflow
 */

#ifndef PUSH_RELABEL_MAXFLOW_INTERFACE_H
#define PUSH_RELABEL_MAXFLOW_INTERFACE_H

#include "types.cpp"

typedef int (*push_relabel_maxflow_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct push_relabel_maxflow_vtable {
    int (*init)(push_relabel_maxflow_state_t* state, const push_relabel_maxflow_config_t* cfg);
    int (*execute)(push_relabel_maxflow_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(push_relabel_maxflow_state_t* state);
    int (*destroy)(push_relabel_maxflow_state_t* state);
} push_relabel_maxflow_vtable_t;

#endif /* PUSH_RELABEL_MAXFLOW_INTERFACE_H */
