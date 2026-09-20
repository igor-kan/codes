#pragma once
#include <vector>
#include <cmath>
#include <functional>

namespace NumericalRecipes {

inline double integrate_gauss_legendre_3pt(std::function<double(double)> f, double a, double b) {
    // 3-point Gauss-Legendre nodes on [-1, 1]
    const double x1 = -std::sqrt(3.0 / 5.0);
    const double x2 = 0.0;
    const double x3 = std::sqrt(3.0 / 5.0);
    const double w1 = 5.0 / 9.0;
    const double w2 = 8.0 / 9.0;
    const double w3 = 5.0 / 9.0;

    auto map_x = [a, b](double xi) { return 0.5 * ((b - a) * xi + (b + a)); };
    double sum = w1 * f(map_x(x1)) + w2 * f(map_x(x2)) + w3 * f(map_x(x3));
    return 0.5 * (b - a) * sum;
}

} // namespace NumericalRecipes
