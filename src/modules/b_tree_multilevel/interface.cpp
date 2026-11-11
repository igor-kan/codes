/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Multi-Level Balanced B-Tree with Node Split-Merge.
 * Module: b_tree_multilevel
 */

#ifndef B_TREE_MULTILEVEL_INTERFACE_H
#define B_TREE_MULTILEVEL_INTERFACE_H

#include "types.cpp"

typedef int (*b_tree_multilevel_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct b_tree_multilevel_vtable {
    int (*init)(b_tree_multilevel_state_t* state, const b_tree_multilevel_config_t* cfg);
    int (*execute)(b_tree_multilevel_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(b_tree_multilevel_state_t* state);
    int (*destroy)(b_tree_multilevel_state_t* state);
} b_tree_multilevel_vtable_t;

#endif /* B_TREE_MULTILEVEL_INTERFACE_H */
