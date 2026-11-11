/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Karatsuba Divide-and-Conquer Polynomial Multiplication.
 * Module: karatsuba_poly_mul
 */

typedef enum karatsuba_poly_mul_error_code {
    KARATSUBA_POLY_MUL_STATUS_OK = 0,
    KARATSUBA_POLY_MUL_ERR_NULL_PTR = -20,
    KARATSUBA_POLY_MUL_ERR_OUT_OF_BOUNDS = -21,
    KARATSUBA_POLY_MUL_ERR_DIVERGENCE = -22
} karatsuba_poly_mul_error_code_t;

const char* karatsuba_poly_mul_error_message(karatsuba_poly_mul_error_code_t code) {
    switch (code) {
        case KARATSUBA_POLY_MUL_STATUS_OK: return "Operational success";
        case KARATSUBA_POLY_MUL_ERR_NULL_PTR: return "Null pointer argument";
        case KARATSUBA_POLY_MUL_ERR_OUT_OF_BOUNDS: return "Buffer boundary exceeded";
        case KARATSUBA_POLY_MUL_ERR_DIVERGENCE: return "Numerical divergence detected";
        default: return "Unspecified error code";
    }
}
