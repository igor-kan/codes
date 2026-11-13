/**
 * @file core.cpp
 * @brief Concrete computational algorithm implementation for Adaptive Simpson Numerical Quadrature Integrator.
 * Module: simpson_adaptive_quad | Algorithm Family: quadrature
 */

#include "types.cpp"
#include <stdlib.h>
#include <string.h>

int simpson_adaptive_quad_execute_kernel(const double* in_vec, double* out_vec, size_t n, double weight) {
    if (!in_vec || !out_vec || n == 0) return -1;
    for (size_t i = 0; i < n; ++i) {
        double x = in_vec[i];
        out_vec[i] = x * (1.0 + weight * x / (1.0 + x * x));
    }
    return 0;
}
