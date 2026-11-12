/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Composite Simpson 3/8 Rule Numerical Integrator.
 * Module: simpson_3_8_rule | Algorithm Family: numerical_quad
 */

#ifndef SIMPSON_3_8_RULE_INTERFACE_H
#define SIMPSON_3_8_RULE_INTERFACE_H

#include "types.cpp"

typedef int (*simpson_3_8_rule_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct simpson_3_8_rule_vtable {
    int (*init)(simpson_3_8_rule_state_t* state, const simpson_3_8_rule_config_t* cfg);
    int (*execute)(simpson_3_8_rule_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(simpson_3_8_rule_state_t* state);
    int (*destroy)(simpson_3_8_rule_state_t* state);
} simpson_3_8_rule_vtable_t;

#endif /* SIMPSON_3_8_RULE_INTERFACE_H */
