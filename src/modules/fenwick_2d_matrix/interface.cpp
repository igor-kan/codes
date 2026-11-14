/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for 2D Binary Indexed Tree (Fenwick Matrix) Range Updater.
 * Module: fenwick_2d_matrix | Algorithm Family: fenwick_2d
 */

#ifndef FENWICK_2D_MATRIX_INTERFACE_H
#define FENWICK_2D_MATRIX_INTERFACE_H

#include "types.cpp"

typedef int (*fenwick_2d_matrix_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct fenwick_2d_matrix_vtable {
    int (*init)(fenwick_2d_matrix_state_t* state, const fenwick_2d_matrix_config_t* cfg);
    int (*execute)(fenwick_2d_matrix_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(fenwick_2d_matrix_state_t* state);
    int (*destroy)(fenwick_2d_matrix_state_t* state);
} fenwick_2d_matrix_vtable_t;

#endif /* FENWICK_2D_MATRIX_INTERFACE_H */
