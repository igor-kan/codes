/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Ukkonen Linear-Time Online Suffix Tree Construction.
 * Module: suffix_tree_ukkonen
 */

#ifndef SUFFIX_TREE_UKKONEN_INTERFACE_H
#define SUFFIX_TREE_UKKONEN_INTERFACE_H

#include "types.cpp"

typedef int (*suffix_tree_ukkonen_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct suffix_tree_ukkonen_vtable {
    int (*init)(suffix_tree_ukkonen_state_t* state, const suffix_tree_ukkonen_config_t* cfg);
    int (*execute)(suffix_tree_ukkonen_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(suffix_tree_ukkonen_state_t* state);
    int (*destroy)(suffix_tree_ukkonen_state_t* state);
} suffix_tree_ukkonen_vtable_t;

#endif /* SUFFIX_TREE_UKKONEN_INTERFACE_H */
