/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Boole 5-Point Closed Newton-Cotes Numerical Quadrature.
 * Module: simpson_boole_quadrature
 */

typedef enum simpson_boole_quadrature_error_status {
    SIMPSON_BOOLE_QUADRATURE_OK = 0,
    SIMPSON_BOOLE_QUADRATURE_ERR_INVALID_PARAM = -10,
    SIMPSON_BOOLE_QUADRATURE_ERR_CAPACITY_LIMIT = -11,
    SIMPSON_BOOLE_QUADRATURE_ERR_NUMERICAL_FAULT = -12
} simpson_boole_quadrature_error_status_t;

const char* simpson_boole_quadrature_error_string(simpson_boole_quadrature_error_status_t err) {
    switch (err) {
        case SIMPSON_BOOLE_QUADRATURE_OK: return "Operational success";
        case SIMPSON_BOOLE_QUADRATURE_ERR_INVALID_PARAM: return "Parameter domain precondition violated";
        case SIMPSON_BOOLE_QUADRATURE_ERR_CAPACITY_LIMIT: return "Buffer capacity boundary reached";
        case SIMPSON_BOOLE_QUADRATURE_ERR_NUMERICAL_FAULT: return "Numerical computation anomaly";
        default: return "Unknown module error code";
    }
}
