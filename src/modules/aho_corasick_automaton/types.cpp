/**
 * @file types.cpp
 * @brief Core types and configuration for Aho-Corasick Multi-Pattern String Matching Automaton.
 * Module: aho_corasick_automaton
 */

#ifndef AHO_CORASICK_AUTOMATON_TYPES_H
#define AHO_CORASICK_AUTOMATON_TYPES_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#define AHO_CORASICK_AUTOMATON_ALIGNMENT 64
#define AHO_CORASICK_AUTOMATON_DEFAULT_SZ 8192

typedef struct aho_corasick_automaton_config {
    size_t capacity;
    double tolerance;
    uint32_t flags;
} aho_corasick_automaton_config_t;

typedef struct aho_corasick_automaton_state {
    void* buffer;
    size_t count;
    uint64_t cycles;
    aho_corasick_automaton_config_t config;
} aho_corasick_automaton_state_t;

#endif /* AHO_CORASICK_AUTOMATON_TYPES_H */
