/**
 * @file interface.cpp
 * @brief Abstract contracts and prototypes for Ternary Search Trie Compact String Dictionary.
 * Module: ternary_search_tree
 */

#ifndef TERNARY_SEARCH_TREE_INTERFACE_H
#define TERNARY_SEARCH_TREE_INTERFACE_H

#include "types.cpp"

typedef int (*ternary_search_tree_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct ternary_search_tree_vtable {
    int (*init)(ternary_search_tree_state_t* state, const ternary_search_tree_config_t* cfg);
    int (*execute)(ternary_search_tree_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*destroy)(ternary_search_tree_state_t* state);
} ternary_search_tree_vtable_t;

#endif /* TERNARY_SEARCH_TREE_INTERFACE_H */
