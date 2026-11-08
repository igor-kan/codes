/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Yaroslavskiy Dual-Pivot Vectorized Quicksort.
 * Module: quicksort_dual_pivot
 */

#ifndef QUICKSORT_DUAL_PIVOT_INTERFACE_H
#define QUICKSORT_DUAL_PIVOT_INTERFACE_H

#include "types.cpp"

typedef int (*quicksort_dual_pivot_transform_fn)(const double* in_data, double* out_data, size_t n);

typedef struct quicksort_dual_pivot_interface {
    int (*init)(quicksort_dual_pivot_state_t* state, const quicksort_dual_pivot_config_t* cfg);
    int (*execute)(quicksort_dual_pivot_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(quicksort_dual_pivot_state_t* state);
    int (*destroy)(quicksort_dual_pivot_state_t* state);
} quicksort_dual_pivot_interface_t;

#endif /* QUICKSORT_DUAL_PIVOT_INTERFACE_H */
