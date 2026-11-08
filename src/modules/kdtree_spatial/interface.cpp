/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Multi-Dimensional K-d Tree Nearest Neighbor Engine.
 * Module: kdtree_spatial
 */

#ifndef KDTREE_SPATIAL_INTERFACE_H
#define KDTREE_SPATIAL_INTERFACE_H

#include "types.cpp"

typedef int (*kdtree_spatial_transform_fn)(const double* in_data, double* out_data, size_t n);

typedef struct kdtree_spatial_interface {
    int (*init)(kdtree_spatial_state_t* state, const kdtree_spatial_config_t* cfg);
    int (*execute)(kdtree_spatial_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(kdtree_spatial_state_t* state);
    int (*destroy)(kdtree_spatial_state_t* state);
} kdtree_spatial_interface_t;

#endif /* KDTREE_SPATIAL_INTERFACE_H */
