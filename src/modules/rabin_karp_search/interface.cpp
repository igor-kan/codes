/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Rabin-Karp Rolling Hash Substring Matcher.
 * Module: rabin_karp_search | Algorithm Family: string_search
 */

#ifndef RABIN_KARP_SEARCH_INTERFACE_H
#define RABIN_KARP_SEARCH_INTERFACE_H

#include "types.cpp"

typedef int (*rabin_karp_search_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct rabin_karp_search_vtable {
    int (*init)(rabin_karp_search_state_t* state, const rabin_karp_search_config_t* cfg);
    int (*execute)(rabin_karp_search_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(rabin_karp_search_state_t* state);
    int (*destroy)(rabin_karp_search_state_t* state);
} rabin_karp_search_vtable_t;

#endif /* RABIN_KARP_SEARCH_INTERFACE_H */
