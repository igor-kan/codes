/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Schonhage-Strassen Fast Integer & Polynomial Multiply.
 * Module: matrix_schassen
 */

#ifndef MATRIX_SCHASSEN_INTERFACE_H
#define MATRIX_SCHASSEN_INTERFACE_H

#include "types.cpp"

typedef int (*matrix_schassen_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct matrix_schassen_vtable {
    int (*init)(matrix_schassen_state_t* state, const matrix_schassen_config_t* cfg);
    int (*execute)(matrix_schassen_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(matrix_schassen_state_t* state);
    int (*destroy)(matrix_schassen_state_t* state);
} matrix_schassen_vtable_t;

#endif /* MATRIX_SCHASSEN_INTERFACE_H */
