#include "gaussian_quadrature.hpp"
#include <cmath>

double integrate_gauss_3point(std::function<double(double)> f, double a, double b) {
    const double x[3] = {-std::sqrt(3.0 / 5.0), 0.0, std::sqrt(3.0 / 5.0)};
    const double w[3] = {5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0};
    
    double half_len = 0.5 * (b - a);
    double mid = 0.5 * (a + b);
    double sum = 0.0;
    
    for (int i = 0; i < 3; ++i) {
        sum += w[i] * f(mid + half_len * x[i]);
    }
    return half_len * sum;
}
