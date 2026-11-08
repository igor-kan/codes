/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Self-Balancing AVL Search Tree with Rotations.
 * Module: avl_balanced_tree
 */

#ifndef AVL_BALANCED_TREE_INTERFACE_H
#define AVL_BALANCED_TREE_INTERFACE_H

#include "types.cpp"

typedef int (*avl_balanced_tree_transform_fn)(const double* in_data, double* out_data, size_t n);

typedef struct avl_balanced_tree_interface {
    int (*init)(avl_balanced_tree_state_t* state, const avl_balanced_tree_config_t* cfg);
    int (*execute)(avl_balanced_tree_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(avl_balanced_tree_state_t* state);
    int (*destroy)(avl_balanced_tree_state_t* state);
} avl_balanced_tree_interface_t;

#endif /* AVL_BALANCED_TREE_INTERFACE_H */
