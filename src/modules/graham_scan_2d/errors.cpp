/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Graham Scan 2D Convex Hull Vectorized Geometry.
 * Module: graham_scan_2d
 */

typedef enum graham_scan_2d_error {
    GRAHAM_SCAN_2D_SUCCESS = 0,
    GRAHAM_SCAN_2D_ERR_INVALID_INPUT = -1,
    GRAHAM_SCAN_2D_ERR_BUFFER_OVERFLOW = -2,
    GRAHAM_SCAN_2D_ERR_CONVERGENCE_FAIL = -3
} graham_scan_2d_error_t;

const char* graham_scan_2d_str_error(graham_scan_2d_error_t code) {
    switch (code) {
        case GRAHAM_SCAN_2D_SUCCESS: return "Operation completed successfully";
        case GRAHAM_SCAN_2D_ERR_INVALID_INPUT: return "Input argument violates domain preconditions";
        case GRAHAM_SCAN_2D_ERR_BUFFER_OVERFLOW: return "Output buffer capacity exceeded";
        case GRAHAM_SCAN_2D_ERR_CONVERGENCE_FAIL: return "Numerical algorithm failed to converge within limit";
        default: return "Unrecognized error code";
    }
}
