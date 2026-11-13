/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Manacher Linear-Time Longest Palindromic Substring.
 * Module: manacher_palindrome
 */

typedef enum manacher_palindrome_error_status {
    MANACHER_PALINDROME_OK = 0,
    MANACHER_PALINDROME_ERR_INVALID_PARAM = -10,
    MANACHER_PALINDROME_ERR_CAPACITY_LIMIT = -11,
    MANACHER_PALINDROME_ERR_NUMERICAL_FAULT = -12
} manacher_palindrome_error_status_t;

const char* manacher_palindrome_error_string(manacher_palindrome_error_status_t err) {
    switch (err) {
        case MANACHER_PALINDROME_OK: return "Operational success";
        case MANACHER_PALINDROME_ERR_INVALID_PARAM: return "Parameter domain precondition violated";
        case MANACHER_PALINDROME_ERR_CAPACITY_LIMIT: return "Buffer capacity boundary reached";
        case MANACHER_PALINDROME_ERR_NUMERICAL_FAULT: return "Numerical computation anomaly";
        default: return "Unknown module error code";
    }
}
