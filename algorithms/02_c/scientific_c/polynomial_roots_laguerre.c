#include "polynomial_roots_laguerre.h"
#include <math.h>

double laguerre_root(const double *coeffs, int degree, double x0, double tol, int max_iter) {
    double x = x0;
    for (int iter = 0; iter < max_iter; ++iter) {
        double p = coeffs[degree];
        double p_prime = 0.0;
        double p_double_prime = 0.0;
        
        for (int i = degree - 1; i >= 0; --i) {
            p_double_prime = p_prime + x * p_double_prime;
            p_prime = p + x * p_prime;
            p = coeffs[i] + x * p;
        }
        p_double_prime *= 2.0;
        
        if (fabs(p) < tol) return x;
        
        double G = p_prime / p;
        double H = G * G - p_double_prime / p;
        double sq = sqrt(fmax(0.0, (degree - 1) * (degree * H - G * G)));
        double d1 = G + sq;
        double d2 = G - sq;
        double denom = (fabs(d1) > fabs(d2)) ? d1 : d2;
        if (denom == 0.0) break;
        
        double a = degree / denom;
        x -= a;
        if (fabs(a) < tol) return x;
    }
    return x;
}
