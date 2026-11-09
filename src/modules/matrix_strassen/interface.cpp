/**
 * @file interface.cpp
 * @brief Abstract contracts and prototypes for Strassen Sub-Cubic Fast Matrix Multiplication.
 * Module: matrix_strassen
 */

#ifndef MATRIX_STRASSEN_INTERFACE_H
#define MATRIX_STRASSEN_INTERFACE_H

#include "types.cpp"

typedef int (*matrix_strassen_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct matrix_strassen_vtable {
    int (*init)(matrix_strassen_state_t* state, const matrix_strassen_config_t* cfg);
    int (*execute)(matrix_strassen_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*destroy)(matrix_strassen_state_t* state);
} matrix_strassen_vtable_t;

#endif /* MATRIX_STRASSEN_INTERFACE_H */
