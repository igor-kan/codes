/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Heavy-Light Decomposition for Tree Path Invariant Queries.
 * Module: heavy_light_decomp
 */

#ifndef HEAVY_LIGHT_DECOMP_INTERFACE_H
#define HEAVY_LIGHT_DECOMP_INTERFACE_H

#include "types.cpp"

typedef int (*heavy_light_decomp_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct heavy_light_decomp_vtable {
    int (*init)(heavy_light_decomp_state_t* state, const heavy_light_decomp_config_t* cfg);
    int (*execute)(heavy_light_decomp_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(heavy_light_decomp_state_t* state);
    int (*destroy)(heavy_light_decomp_state_t* state);
} heavy_light_decomp_vtable_t;

#endif /* HEAVY_LIGHT_DECOMP_INTERFACE_H */
