/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Brent Teleporting Tortoise and Hare Cycle Detector.
 * Module: brent_cycle_find | Algorithm Family: cycle_find
 */

#ifndef BRENT_CYCLE_FIND_INTERFACE_H
#define BRENT_CYCLE_FIND_INTERFACE_H

#include "types.cpp"

typedef int (*brent_cycle_find_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct brent_cycle_find_vtable {
    int (*init)(brent_cycle_find_state_t* state, const brent_cycle_find_config_t* cfg);
    int (*execute)(brent_cycle_find_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(brent_cycle_find_state_t* state);
    int (*destroy)(brent_cycle_find_state_t* state);
} brent_cycle_find_vtable_t;

#endif /* BRENT_CYCLE_FIND_INTERFACE_H */
