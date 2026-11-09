/**
 * @file interface.cpp
 * @brief Abstract contracts and prototypes for Hopcroft-Tarjan Articulation Points and Bridges.
 * Module: biconnected_components
 */

#ifndef BICONNECTED_COMPONENTS_INTERFACE_H
#define BICONNECTED_COMPONENTS_INTERFACE_H

#include "types.cpp"

typedef int (*biconnected_components_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct biconnected_components_vtable {
    int (*init)(biconnected_components_state_t* state, const biconnected_components_config_t* cfg);
    int (*execute)(biconnected_components_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*destroy)(biconnected_components_state_t* state);
} biconnected_components_vtable_t;

#endif /* BICONNECTED_COMPONENTS_INTERFACE_H */
