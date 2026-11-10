/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Heavy-Light Decomposition for Tree Path Invariant Queries.
 * Module: heavy_light_decomp
 */

typedef enum heavy_light_decomp_error_code {
    HEAVY_LIGHT_DECOMP_STATUS_OK = 0,
    HEAVY_LIGHT_DECOMP_ERR_NULL_PTR = -10,
    HEAVY_LIGHT_DECOMP_ERR_OUT_OF_BOUNDS = -11,
    HEAVY_LIGHT_DECOMP_ERR_DIVERGENCE = -12
} heavy_light_decomp_error_code_t;

const char* heavy_light_decomp_error_message(heavy_light_decomp_error_code_t code) {
    switch (code) {
        case HEAVY_LIGHT_DECOMP_STATUS_OK: return "Operational success";
        case HEAVY_LIGHT_DECOMP_ERR_NULL_PTR: return "Null pointer argument";
        case HEAVY_LIGHT_DECOMP_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case HEAVY_LIGHT_DECOMP_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
