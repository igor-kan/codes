/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Wagner-Fischer Dynamic Programming Edit Distance.
 * Module: levenshtein_distance
 */

typedef enum levenshtein_distance_error {
    LEVENSHTEIN_DISTANCE_SUCCESS = 0,
    LEVENSHTEIN_DISTANCE_ERR_INVALID_INPUT = -1,
    LEVENSHTEIN_DISTANCE_ERR_BUFFER_OVERFLOW = -2,
    LEVENSHTEIN_DISTANCE_ERR_CONVERGENCE_FAIL = -3
} levenshtein_distance_error_t;

const char* levenshtein_distance_str_error(levenshtein_distance_error_t code) {
    switch (code) {
        case LEVENSHTEIN_DISTANCE_SUCCESS: return "Operation completed successfully";
        case LEVENSHTEIN_DISTANCE_ERR_INVALID_INPUT: return "Input argument violates domain preconditions";
        case LEVENSHTEIN_DISTANCE_ERR_BUFFER_OVERFLOW: return "Output buffer capacity exceeded";
        case LEVENSHTEIN_DISTANCE_ERR_CONVERGENCE_FAIL: return "Numerical algorithm failed to converge within limit";
        default: return "Unrecognized error code";
    }
}
