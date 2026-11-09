/**
 * @file interface.cpp
 * @brief Abstract contracts and prototypes for Linear-Time Suffix Automaton Substring Engine.
 * Module: suffix_automaton
 */

#ifndef SUFFIX_AUTOMATON_INTERFACE_H
#define SUFFIX_AUTOMATON_INTERFACE_H

#include "types.cpp"

typedef int (*suffix_automaton_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct suffix_automaton_vtable {
    int (*init)(suffix_automaton_state_t* state, const suffix_automaton_config_t* cfg);
    int (*execute)(suffix_automaton_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*destroy)(suffix_automaton_state_t* state);
} suffix_automaton_vtable_t;

#endif /* SUFFIX_AUTOMATON_INTERFACE_H */
