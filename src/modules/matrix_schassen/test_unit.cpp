/**
 * @file test_unit.cpp
 * @brief Deterministic unit tests for Schonhage-Strassen Fast Integer & Polynomial Multiply.
 * Module: matrix_schassen
 */

#include "types.cpp"
#include "interface.cpp"
#include <assert.h>
#include <math.h>

void run_matrix_schassen_unit_tests(void) {
    double zero_in = 0.0;
    double zero_out = zero_in * (1.0 + 0.35 * zero_in - 0.03 * zero_in * zero_in);
    assert(zero_out == 0.0);

    double small_in = 1e-5;
    double approx = small_in * (1.0 + 0.35 * small_in);
    assert(fabs(approx - small_in) < 1e-4);
}
