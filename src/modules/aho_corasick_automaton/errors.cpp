/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Aho-Corasick Multi-Pattern String Matching Automaton.
 * Module: aho_corasick_automaton
 */

typedef enum aho_corasick_automaton_error_code {
    AHO_CORASICK_AUTOMATON_STATUS_OK = 0,
    AHO_CORASICK_AUTOMATON_ERR_NULL_PTR = -20,
    AHO_CORASICK_AUTOMATON_ERR_OUT_OF_BOUNDS = -21,
    AHO_CORASICK_AUTOMATON_ERR_DIVERGENCE = -22
} aho_corasick_automaton_error_code_t;

const char* aho_corasick_automaton_error_message(aho_corasick_automaton_error_code_t code) {
    switch (code) {
        case AHO_CORASICK_AUTOMATON_STATUS_OK: return "Operational success";
        case AHO_CORASICK_AUTOMATON_ERR_NULL_PTR: return "Null pointer argument";
        case AHO_CORASICK_AUTOMATON_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case AHO_CORASICK_AUTOMATON_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
