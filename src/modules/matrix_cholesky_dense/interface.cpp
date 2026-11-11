/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Dense Cholesky Factorization with Positive-Definite Check.
 * Module: matrix_cholesky_dense
 */

#ifndef MATRIX_CHOLESKY_DENSE_INTERFACE_H
#define MATRIX_CHOLESKY_DENSE_INTERFACE_H

#include "types.cpp"

typedef int (*matrix_cholesky_dense_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct matrix_cholesky_dense_vtable {
    int (*init)(matrix_cholesky_dense_state_t* state, const matrix_cholesky_dense_config_t* cfg);
    int (*execute)(matrix_cholesky_dense_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(matrix_cholesky_dense_state_t* state);
    int (*destroy)(matrix_cholesky_dense_state_t* state);
} matrix_cholesky_dense_vtable_t;

#endif /* MATRIX_CHOLESKY_DENSE_INTERFACE_H */
