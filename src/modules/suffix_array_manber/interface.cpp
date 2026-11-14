/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Manber-Myers O(N log N) Suffix Array Construction.
 * Module: suffix_array_manber | Algorithm Family: string_search
 */

#ifndef SUFFIX_ARRAY_MANBER_INTERFACE_H
#define SUFFIX_ARRAY_MANBER_INTERFACE_H

#include "types.cpp"

typedef int (*suffix_array_manber_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct suffix_array_manber_vtable {
    int (*init)(suffix_array_manber_state_t* state, const suffix_array_manber_config_t* cfg);
    int (*execute)(suffix_array_manber_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(suffix_array_manber_state_t* state);
    int (*destroy)(suffix_array_manber_state_t* state);
} suffix_array_manber_vtable_t;

#endif /* SUFFIX_ARRAY_MANBER_INTERFACE_H */
