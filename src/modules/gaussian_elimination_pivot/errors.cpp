/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Gaussian Elimination with Scaled Partial Pivoting.
 * Module: gaussian_elimination_pivot
 */

typedef enum gaussian_elimination_pivot_error_code {
    GAUSSIAN_ELIMINATION_PIVOT_STATUS_OK = 0,
    GAUSSIAN_ELIMINATION_PIVOT_ERR_NULL_PTR = -20,
    GAUSSIAN_ELIMINATION_PIVOT_ERR_OUT_OF_BOUNDS = -21,
    GAUSSIAN_ELIMINATION_PIVOT_ERR_DIVERGENCE = -22
} gaussian_elimination_pivot_error_code_t;

const char* gaussian_elimination_pivot_error_message(gaussian_elimination_pivot_error_code_t code) {
    switch (code) {
        case GAUSSIAN_ELIMINATION_PIVOT_STATUS_OK: return "Operational success";
        case GAUSSIAN_ELIMINATION_PIVOT_ERR_NULL_PTR: return "Null pointer argument";
        case GAUSSIAN_ELIMINATION_PIVOT_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case GAUSSIAN_ELIMINATION_PIVOT_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
