/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Dense Cholesky Factorization with Positive-Definite Check.
 * Module: matrix_cholesky_dense
 */

typedef enum matrix_cholesky_dense_error_code {
    MATRIX_CHOLESKY_DENSE_STATUS_OK = 0,
    MATRIX_CHOLESKY_DENSE_ERR_NULL_PTR = -20,
    MATRIX_CHOLESKY_DENSE_ERR_OUT_OF_BOUNDS = -21,
    MATRIX_CHOLESKY_DENSE_ERR_DIVERGENCE = -22
} matrix_cholesky_dense_error_code_t;

const char* matrix_cholesky_dense_error_message(matrix_cholesky_dense_error_code_t code) {
    switch (code) {
        case MATRIX_CHOLESKY_DENSE_STATUS_OK: return "Operational success";
        case MATRIX_CHOLESKY_DENSE_ERR_NULL_PTR: return "Null pointer argument";
        case MATRIX_CHOLESKY_DENSE_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case MATRIX_CHOLESKY_DENSE_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
