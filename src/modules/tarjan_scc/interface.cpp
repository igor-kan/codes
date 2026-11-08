/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Tarjan Strongly Connected Components Low-Link Graph Engine.
 * Module: tarjan_scc
 */

#ifndef TARJAN_SCC_INTERFACE_H
#define TARJAN_SCC_INTERFACE_H

#include "types.cpp"

typedef int (*tarjan_scc_transform_fn)(const double* in_data, double* out_data, size_t n);

typedef struct tarjan_scc_interface {
    int (*init)(tarjan_scc_state_t* state, const tarjan_scc_config_t* cfg);
    int (*execute)(tarjan_scc_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(tarjan_scc_state_t* state);
    int (*destroy)(tarjan_scc_state_t* state);
} tarjan_scc_interface_t;

#endif /* TARJAN_SCC_INTERFACE_H */
