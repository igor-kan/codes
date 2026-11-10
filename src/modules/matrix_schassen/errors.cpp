/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Schonhage-Strassen Fast Integer & Polynomial Multiply.
 * Module: matrix_schassen
 */

typedef enum matrix_schassen_error_code {
    MATRIX_SCHASSEN_STATUS_OK = 0,
    MATRIX_SCHASSEN_ERR_NULL_PTR = -10,
    MATRIX_SCHASSEN_ERR_OUT_OF_BOUNDS = -11,
    MATRIX_SCHASSEN_ERR_DIVERGENCE = -12
} matrix_schassen_error_code_t;

const char* matrix_schassen_error_message(matrix_schassen_error_code_t code) {
    switch (code) {
        case MATRIX_SCHASSEN_STATUS_OK: return "Operational success";
        case MATRIX_SCHASSEN_ERR_NULL_PTR: return "Null pointer argument";
        case MATRIX_SCHASSEN_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case MATRIX_SCHASSEN_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
