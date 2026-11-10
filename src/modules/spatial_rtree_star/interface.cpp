/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for R*-Tree Spatial Index with Topological Reinsertion.
 * Module: spatial_rtree_star
 */

#ifndef SPATIAL_RTREE_STAR_INTERFACE_H
#define SPATIAL_RTREE_STAR_INTERFACE_H

#include "types.cpp"

typedef int (*spatial_rtree_star_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct spatial_rtree_star_vtable {
    int (*init)(spatial_rtree_star_state_t* state, const spatial_rtree_star_config_t* cfg);
    int (*execute)(spatial_rtree_star_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(spatial_rtree_star_state_t* state);
    int (*destroy)(spatial_rtree_star_state_t* state);
} spatial_rtree_star_vtable_t;

#endif /* SPATIAL_RTREE_STAR_INTERFACE_H */
