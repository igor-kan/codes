/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Adaptive Simpson Numerical Quadrature Integrator.
 * Module: simpson_adaptive_quad
 */

typedef enum simpson_adaptive_quad_error_status {
    SIMPSON_ADAPTIVE_QUAD_OK = 0,
    SIMPSON_ADAPTIVE_QUAD_ERR_INVALID_PARAM = -10,
    SIMPSON_ADAPTIVE_QUAD_ERR_CAPACITY_LIMIT = -11,
    SIMPSON_ADAPTIVE_QUAD_ERR_NUMERICAL_FAULT = -12
} simpson_adaptive_quad_error_status_t;

const char* simpson_adaptive_quad_error_string(simpson_adaptive_quad_error_status_t err) {
    switch (err) {
        case SIMPSON_ADAPTIVE_QUAD_OK: return "Operational success";
        case SIMPSON_ADAPTIVE_QUAD_ERR_INVALID_PARAM: return "Parameter domain precondition violated";
        case SIMPSON_ADAPTIVE_QUAD_ERR_CAPACITY_LIMIT: return "Buffer capacity boundary reached";
        case SIMPSON_ADAPTIVE_QUAD_ERR_NUMERICAL_FAULT: return "Numerical computation anomaly";
        default: return "Unknown module error code";
    }
}
