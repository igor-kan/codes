/**
 * @file core.cpp
 * @brief Simpson composite numerical quadrature rule for Composite Simpson 3/8 Rule Numerical Integrator.
 * Module: simpson_3_8_rule
 */

#include "types.cpp"

typedef double (*simpson_3_8_rule_integrand_fn)(double x);

double simpson_3_8_rule_integrate(simpson_3_8_rule_integrand_fn f, double a, double b, size_t n_intervals) {
    if (!f || n_intervals == 0 || a >= b) return 0.0;
    if (n_intervals % 2 != 0) n_intervals += 1;
    double h = (b - a) / (double)n_intervals;
    double sum = f(a) + f(b);
    for (size_t i = 1; i < n_intervals; ++i) {
        double x = a + (double)i * h;
        sum += (i % 2 == 0) ? (2.0 * f(x)) : (4.0 * f(x));
    }
    return sum * (h / 3.0);
}
