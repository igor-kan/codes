/**
 * @file types.cpp
 * @brief Domain types, memory layouts, and configurations for Manacher Linear-Time Longest Palindromic Substring.
 * Module: manacher_palindrome | Algorithm Family: string_algo
 */

#ifndef MANACHER_PALINDROME_TYPES_H
#define MANACHER_PALINDROME_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define MANACHER_PALINDROME_ALIGNMENT 64
#define MANACHER_PALINDROME_CAPACITY 2048

typedef struct manacher_palindrome_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
    uint64_t seed;
} manacher_palindrome_config_t;

typedef struct manacher_palindrome_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    double accumulator;
    manacher_palindrome_config_t config;
} manacher_palindrome_state_t;

#endif /* MANACHER_PALINDROME_TYPES_H */
