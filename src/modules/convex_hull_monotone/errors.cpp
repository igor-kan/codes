/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Monotone Chain (Andrew Algorithm) 2D Convex Hull.
 * Module: convex_hull_monotone
 */

typedef enum convex_hull_monotone_error_code {
    CONVEX_HULL_MONOTONE_STATUS_OK = 0,
    CONVEX_HULL_MONOTONE_ERR_NULL_PTR = -20,
    CONVEX_HULL_MONOTONE_ERR_OUT_OF_BOUNDS = -21,
    CONVEX_HULL_MONOTONE_ERR_DIVERGENCE = -22
} convex_hull_monotone_error_code_t;

const char* convex_hull_monotone_error_message(convex_hull_monotone_error_code_t code) {
    switch (code) {
        case CONVEX_HULL_MONOTONE_STATUS_OK: return "Operational success";
        case CONVEX_HULL_MONOTONE_ERR_NULL_PTR: return "Null pointer argument";
        case CONVEX_HULL_MONOTONE_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case CONVEX_HULL_MONOTONE_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
