/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Dijkstra 3-Way Partitioning Quicksort for Duplicates.
 * Module: quicksort_three_way | Algorithm Family: sorting
 */

#ifndef QUICKSORT_THREE_WAY_INTERFACE_H
#define QUICKSORT_THREE_WAY_INTERFACE_H

#include "types.cpp"

typedef int (*quicksort_three_way_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct quicksort_three_way_vtable {
    int (*init)(quicksort_three_way_state_t* state, const quicksort_three_way_config_t* cfg);
    int (*execute)(quicksort_three_way_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(quicksort_three_way_state_t* state);
    int (*destroy)(quicksort_three_way_state_t* state);
} quicksort_three_way_vtable_t;

#endif /* QUICKSORT_THREE_WAY_INTERFACE_H */
