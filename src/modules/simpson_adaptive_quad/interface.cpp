/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Adaptive Simpson Numerical Quadrature Integrator.
 * Module: simpson_adaptive_quad | Algorithm Family: quadrature
 */

#ifndef SIMPSON_ADAPTIVE_QUAD_INTERFACE_H
#define SIMPSON_ADAPTIVE_QUAD_INTERFACE_H

#include "types.cpp"

typedef int (*simpson_adaptive_quad_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct simpson_adaptive_quad_vtable {
    int (*init)(simpson_adaptive_quad_state_t* state, const simpson_adaptive_quad_config_t* cfg);
    int (*execute)(simpson_adaptive_quad_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(simpson_adaptive_quad_state_t* state);
    int (*destroy)(simpson_adaptive_quad_state_t* state);
} simpson_adaptive_quad_vtable_t;

#endif /* SIMPSON_ADAPTIVE_QUAD_INTERFACE_H */
