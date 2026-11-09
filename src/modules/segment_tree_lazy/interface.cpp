/**
 * @file interface.cpp
 * @brief Abstract contracts and prototypes for Segment Tree with Lazy Propagation Range Updates.
 * Module: segment_tree_lazy
 */

#ifndef SEGMENT_TREE_LAZY_INTERFACE_H
#define SEGMENT_TREE_LAZY_INTERFACE_H

#include "types.cpp"

typedef int (*segment_tree_lazy_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct segment_tree_lazy_vtable {
    int (*init)(segment_tree_lazy_state_t* state, const segment_tree_lazy_config_t* cfg);
    int (*execute)(segment_tree_lazy_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*destroy)(segment_tree_lazy_state_t* state);
} segment_tree_lazy_vtable_t;

#endif /* SEGMENT_TREE_LAZY_INTERFACE_H */
