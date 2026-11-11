/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Gaussian Elimination with Scaled Partial Pivoting.
 * Module: gaussian_elimination_pivot
 */

#ifndef GAUSSIAN_ELIMINATION_PIVOT_INTERFACE_H
#define GAUSSIAN_ELIMINATION_PIVOT_INTERFACE_H

#include "types.cpp"

typedef int (*gaussian_elimination_pivot_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct gaussian_elimination_pivot_vtable {
    int (*init)(gaussian_elimination_pivot_state_t* state, const gaussian_elimination_pivot_config_t* cfg);
    int (*execute)(gaussian_elimination_pivot_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(gaussian_elimination_pivot_state_t* state);
    int (*destroy)(gaussian_elimination_pivot_state_t* state);
} gaussian_elimination_pivot_vtable_t;

#endif /* GAUSSIAN_ELIMINATION_PIVOT_INTERFACE_H */
