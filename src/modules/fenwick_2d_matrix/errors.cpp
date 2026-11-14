/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for 2D Binary Indexed Tree (Fenwick Matrix) Range Updater.
 * Module: fenwick_2d_matrix
 */

typedef enum fenwick_2d_matrix_error_status {
    FENWICK_2D_MATRIX_OK = 0,
    FENWICK_2D_MATRIX_ERR_INVALID_PARAM = -10,
    FENWICK_2D_MATRIX_ERR_CAPACITY_LIMIT = -11,
    FENWICK_2D_MATRIX_ERR_NUMERICAL_FAULT = -12
} fenwick_2d_matrix_error_status_t;

const char* fenwick_2d_matrix_error_string(fenwick_2d_matrix_error_status_t err) {
    switch (err) {
        case FENWICK_2D_MATRIX_OK: return "Operational success";
        case FENWICK_2D_MATRIX_ERR_INVALID_PARAM: return "Parameter domain precondition violated";
        case FENWICK_2D_MATRIX_ERR_CAPACITY_LIMIT: return "Buffer capacity boundary reached";
        case FENWICK_2D_MATRIX_ERR_NUMERICAL_FAULT: return "Numerical computation anomaly";
        default: return "Unknown module error code";
    }
}
