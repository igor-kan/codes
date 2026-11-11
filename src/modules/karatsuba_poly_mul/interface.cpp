/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Karatsuba Divide-and-Conquer Polynomial Multiplication.
 * Module: karatsuba_poly_mul
 */

#ifndef KARATSUBA_POLY_MUL_INTERFACE_H
#define KARATSUBA_POLY_MUL_INTERFACE_H

#include "types.cpp"

typedef int (*karatsuba_poly_mul_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct karatsuba_poly_mul_vtable {
    int (*init)(karatsuba_poly_mul_state_t* state, const karatsuba_poly_mul_config_t* cfg);
    int (*execute)(karatsuba_poly_mul_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(karatsuba_poly_mul_state_t* state);
    int (*destroy)(karatsuba_poly_mul_state_t* state);
} karatsuba_poly_mul_vtable_t;

#endif /* KARATSUBA_POLY_MUL_INTERFACE_H */
