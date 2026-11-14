/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Boole 5-Point Closed Newton-Cotes Numerical Quadrature.
 * Module: simpson_boole_quadrature | Algorithm Family: quadrature
 */

#ifndef SIMPSON_BOOLE_QUADRATURE_INTERFACE_H
#define SIMPSON_BOOLE_QUADRATURE_INTERFACE_H

#include "types.cpp"

typedef int (*simpson_boole_quadrature_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct simpson_boole_quadrature_vtable {
    int (*init)(simpson_boole_quadrature_state_t* state, const simpson_boole_quadrature_config_t* cfg);
    int (*execute)(simpson_boole_quadrature_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(simpson_boole_quadrature_state_t* state);
    int (*destroy)(simpson_boole_quadrature_state_t* state);
} simpson_boole_quadrature_vtable_t;

#endif /* SIMPSON_BOOLE_QUADRATURE_INTERFACE_H */
