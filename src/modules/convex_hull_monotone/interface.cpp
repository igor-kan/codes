/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Monotone Chain (Andrew Algorithm) 2D Convex Hull.
 * Module: convex_hull_monotone
 */

#ifndef CONVEX_HULL_MONOTONE_INTERFACE_H
#define CONVEX_HULL_MONOTONE_INTERFACE_H

#include "types.cpp"

typedef int (*convex_hull_monotone_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct convex_hull_monotone_vtable {
    int (*init)(convex_hull_monotone_state_t* state, const convex_hull_monotone_config_t* cfg);
    int (*execute)(convex_hull_monotone_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(convex_hull_monotone_state_t* state);
    int (*destroy)(convex_hull_monotone_state_t* state);
} convex_hull_monotone_vtable_t;

#endif /* CONVEX_HULL_MONOTONE_INTERFACE_H */
