/**
 * @file interface.cpp
 * @brief Abstract contracts and prototypes for Dinic Maximum Flow Network with Level Graphs.
 * Module: max_flow_dinic
 */

#ifndef MAX_FLOW_DINIC_INTERFACE_H
#define MAX_FLOW_DINIC_INTERFACE_H

#include "types.cpp"

typedef int (*max_flow_dinic_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct max_flow_dinic_vtable {
    int (*init)(max_flow_dinic_state_t* state, const max_flow_dinic_config_t* cfg);
    int (*execute)(max_flow_dinic_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*destroy)(max_flow_dinic_state_t* state);
} max_flow_dinic_vtable_t;

#endif /* MAX_FLOW_DINIC_INTERFACE_H */
