/**
 * @file boundary.cpp
 * @brief Boundary validation and exceptional input guarding for Dense Cholesky Factorization with Positive-Definite Check.
 * Module: matrix_cholesky_dense
 */

#include "types.cpp"
#include <math.h>
#include <stdbool.h>

static inline bool matrix_cholesky_dense_is_valid_float(double x) {
    return isfinite(x);
}

static inline double matrix_cholesky_dense_clamp_input(double x, double min_val, double max_val) {
    if (!isfinite(x)) return 0.0;
    if (x < min_val) return min_val;
    if (x > max_val) return max_val;
    return x;
}
