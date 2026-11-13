/**
 * @file interface.cpp
 * @brief Abstract function prototypes and contracts for Manacher Linear-Time Longest Palindromic Substring.
 * Module: manacher_palindrome | Algorithm Family: string_algo
 */

#ifndef MANACHER_PALINDROME_INTERFACE_H
#define MANACHER_PALINDROME_INTERFACE_H

#include "types.cpp"

typedef int (*manacher_palindrome_kernel_fn)(const double* in_vec, double* out_vec, size_t n);

typedef struct manacher_palindrome_vtable {
    int (*init)(manacher_palindrome_state_t* state, const manacher_palindrome_config_t* cfg);
    int (*execute)(manacher_palindrome_state_t* state, const double* in_vec, double* out_vec, size_t n);
    int (*reset)(manacher_palindrome_state_t* state);
    int (*destroy)(manacher_palindrome_state_t* state);
} manacher_palindrome_vtable_t;

#endif /* MANACHER_PALINDROME_INTERFACE_H */
