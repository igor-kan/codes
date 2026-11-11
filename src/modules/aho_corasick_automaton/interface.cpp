/**
 * @file interface.cpp
 * @brief Abstract contracts and operational prototypes for Aho-Corasick Multi-Pattern String Matching Automaton.
 * Module: aho_corasick_automaton
 */

#ifndef AHO_CORASICK_AUTOMATON_INTERFACE_H
#define AHO_CORASICK_AUTOMATON_INTERFACE_H

#include "types.cpp"

typedef int (*aho_corasick_automaton_kernel_fn)(const double* in_data, double* out_data, size_t n);

typedef struct aho_corasick_automaton_vtable {
    int (*init)(aho_corasick_automaton_state_t* state, const aho_corasick_automaton_config_t* cfg);
    int (*execute)(aho_corasick_automaton_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(aho_corasick_automaton_state_t* state);
    int (*destroy)(aho_corasick_automaton_state_t* state);
} aho_corasick_automaton_vtable_t;

#endif /* AHO_CORASICK_AUTOMATON_INTERFACE_H */
