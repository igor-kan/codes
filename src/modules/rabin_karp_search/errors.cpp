/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Rabin-Karp Rolling Hash Substring Matcher.
 * Module: rabin_karp_search
 */

typedef enum rabin_karp_search_error {
    RABIN_KARP_SEARCH_SUCCESS = 0,
    RABIN_KARP_SEARCH_ERR_INVALID_INPUT = -1,
    RABIN_KARP_SEARCH_ERR_BUFFER_OVERFLOW = -2,
    RABIN_KARP_SEARCH_ERR_CONVERGENCE_FAIL = -3
} rabin_karp_search_error_t;

const char* rabin_karp_search_str_error(rabin_karp_search_error_t code) {
    switch (code) {
        case RABIN_KARP_SEARCH_SUCCESS: return "Operation completed successfully";
        case RABIN_KARP_SEARCH_ERR_INVALID_INPUT: return "Input argument violates domain preconditions";
        case RABIN_KARP_SEARCH_ERR_BUFFER_OVERFLOW: return "Output buffer capacity exceeded";
        case RABIN_KARP_SEARCH_ERR_CONVERGENCE_FAIL: return "Numerical algorithm failed to converge within limit";
        default: return "Unrecognized error code";
    }
}
