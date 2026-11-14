/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Manber-Myers O(N log N) Suffix Array Construction.
 * Module: suffix_array_manber
 */

typedef enum suffix_array_manber_error_status {
    SUFFIX_ARRAY_MANBER_OK = 0,
    SUFFIX_ARRAY_MANBER_ERR_INVALID_PARAM = -10,
    SUFFIX_ARRAY_MANBER_ERR_CAPACITY_LIMIT = -11,
    SUFFIX_ARRAY_MANBER_ERR_NUMERICAL_FAULT = -12
} suffix_array_manber_error_status_t;

const char* suffix_array_manber_error_string(suffix_array_manber_error_status_t err) {
    switch (err) {
        case SUFFIX_ARRAY_MANBER_OK: return "Operational success";
        case SUFFIX_ARRAY_MANBER_ERR_INVALID_PARAM: return "Parameter domain precondition violated";
        case SUFFIX_ARRAY_MANBER_ERR_CAPACITY_LIMIT: return "Buffer capacity boundary reached";
        case SUFFIX_ARRAY_MANBER_ERR_NUMERICAL_FAULT: return "Numerical computation anomaly";
        default: return "Unknown module error code";
    }
}
