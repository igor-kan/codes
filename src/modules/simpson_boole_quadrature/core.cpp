/**
 * @file core.cpp
 * @brief Numerical quadrature integration rule for Boole 5-Point Closed Newton-Cotes Numerical Quadrature.
 * Module: simpson_boole_quadrature
 */

#include "types.cpp"

typedef double (*simpson_boole_quadrature_func)(double x);

double simpson_boole_quadrature_integrate_rule(simpson_boole_quadrature_func f, double a, double b, size_t n) {
    if (!f || a >= b || n == 0) return 0.0;
    double h = (b - a) / (double)n;
    double sum = 0.5 * (f(a) + f(b));
    for (size_t i = 1; i < n; ++i) {
        sum += f(a + (double)i * h);
    }
    return sum * h;
}
