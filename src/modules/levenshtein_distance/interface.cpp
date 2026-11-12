/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Wagner-Fischer Dynamic Programming Edit Distance.
 * Module: levenshtein_distance | Algorithm Family: dp_matrix
 */

#ifndef LEVENSHTEIN_DISTANCE_INTERFACE_H
#define LEVENSHTEIN_DISTANCE_INTERFACE_H

#include "types.cpp"

typedef int (*levenshtein_distance_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct levenshtein_distance_vtable {
    int (*init)(levenshtein_distance_state_t* state, const levenshtein_distance_config_t* cfg);
    int (*execute)(levenshtein_distance_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(levenshtein_distance_state_t* state);
    int (*destroy)(levenshtein_distance_state_t* state);
} levenshtein_distance_vtable_t;

#endif /* LEVENSHTEIN_DISTANCE_INTERFACE_H */
