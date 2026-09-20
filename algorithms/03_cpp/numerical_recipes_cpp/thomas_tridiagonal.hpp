#pragma once
#include <vector>
#include <stdexcept>

namespace NumericalRecipes {

inline std::vector<double> solve_tridiagonal(const std::vector<double>& a,
                                             const std::vector<double>& b,
                                             const std::vector<double>& c,
                                             const std::vector<double>& d) {
    size_t n = b.size();
    std::vector<double> c_prime(n - 1, 0.0);
    std::vector<double> d_prime(n, 0.0);

    c_prime[0] = c[0] / b[0];
    d_prime[0] = d[0] / b[0];

    for (size_t i = 1; i < n - 1; ++i) {
        double denom = b[i] - a[i - 1] * c_prime[i - 1];
        c_prime[i] = c[i] / denom;
        d_prime[i] = (d[i] - a[i - 1] * d_prime[i - 1]) / denom;
    }
    d_prime[n - 1] = (d[n - 1] - a[n - 2] * d_prime[n - 2]) / (b[n - 1] - a[n - 2] * c_prime[n - 2]);

    std::vector<double> x(n, 0.0);
    x[n - 1] = d_prime[n - 1];
    for (int i = static_cast<int>(n) - 2; i >= 0; --i) {
        x[i] = d_prime[i] - c_prime[i] * x[i + 1];
    }
    return x;
}

} // namespace NumericalRecipes
