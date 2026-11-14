/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Leaf-Chained B+ Tree Index Structure for Range Scans.
 * Module: b_plus_tree_leaf | Algorithm Family: b_plus_tree
 */

#ifndef B_PLUS_TREE_LEAF_INTERFACE_H
#define B_PLUS_TREE_LEAF_INTERFACE_H

#include "types.cpp"

typedef int (*b_plus_tree_leaf_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct b_plus_tree_leaf_vtable {
    int (*init)(b_plus_tree_leaf_state_t* state, const b_plus_tree_leaf_config_t* cfg);
    int (*execute)(b_plus_tree_leaf_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(b_plus_tree_leaf_state_t* state);
    int (*destroy)(b_plus_tree_leaf_state_t* state);
} b_plus_tree_leaf_vtable_t;

#endif /* B_PLUS_TREE_LEAF_INTERFACE_H */
