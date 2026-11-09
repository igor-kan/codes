/**
 * @file types.cpp
 * @brief Core types and configuration for Linear-Time Suffix Automaton Substring Engine.
 * Module: suffix_automaton
 */

#ifndef SUFFIX_AUTOMATON_TYPES_H
#define SUFFIX_AUTOMATON_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define SUFFIX_AUTOMATON_ALIGNMENT 64
#define SUFFIX_AUTOMATON_CAPACITY 2048

typedef struct suffix_automaton_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} suffix_automaton_config_t;

typedef struct suffix_automaton_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    suffix_automaton_config_t config;
} suffix_automaton_state_t;

#endif /* SUFFIX_AUTOMATON_TYPES_H */
