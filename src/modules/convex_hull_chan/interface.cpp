/**
 * @file interface.cpp
 * @brief Abstract contracts and prototypes for Chan Optimal 2D Convex Hull Geometric Engine.
 * Module: convex_hull_chan
 */

#ifndef CONVEX_HULL_CHAN_INTERFACE_H
#define CONVEX_HULL_CHAN_INTERFACE_H

#include "types.cpp"

typedef int (*convex_hull_chan_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct convex_hull_chan_vtable {
    int (*init)(convex_hull_chan_state_t* state, const convex_hull_chan_config_t* cfg);
    int (*execute)(convex_hull_chan_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*destroy)(convex_hull_chan_state_t* state);
} convex_hull_chan_vtable_t;

#endif /* CONVEX_HULL_CHAN_INTERFACE_H */
