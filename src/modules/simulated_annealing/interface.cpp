/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Continuous Domain Simulated Annealing Global Optimizer.
 * Module: simulated_annealing
 */

#ifndef SIMULATED_ANNEALING_INTERFACE_H
#define SIMULATED_ANNEALING_INTERFACE_H

#include "types.cpp"

typedef int (*simulated_annealing_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct simulated_annealing_vtable {
    int (*init)(simulated_annealing_state_t* state, const simulated_annealing_config_t* cfg);
    int (*execute)(simulated_annealing_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(simulated_annealing_state_t* state);
    int (*destroy)(simulated_annealing_state_t* state);
} simulated_annealing_vtable_t;

#endif /* SIMULATED_ANNEALING_INTERFACE_H */
