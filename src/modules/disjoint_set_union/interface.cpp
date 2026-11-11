/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Disjoint-Set Union (DSU) with Path Compression and Rank.
 * Module: disjoint_set_union
 */

#ifndef DISJOINT_SET_UNION_INTERFACE_H
#define DISJOINT_SET_UNION_INTERFACE_H

#include "types.cpp"

typedef int (*disjoint_set_union_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct disjoint_set_union_vtable {
    int (*init)(disjoint_set_union_state_t* state, const disjoint_set_union_config_t* cfg);
    int (*execute)(disjoint_set_union_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(disjoint_set_union_state_t* state);
    int (*destroy)(disjoint_set_union_state_t* state);
} disjoint_set_union_vtable_t;

#endif /* DISJOINT_SET_UNION_INTERFACE_H */
