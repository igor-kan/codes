#pragma once
#include <vector>
#include <cmath>
#include <stdexcept>

namespace NumericalRecipes {

inline std::vector<std::vector<double>> cholesky_decompose(const std::vector<std::vector<double>>& A) {
    size_t n = A.size();
    std::vector<std::vector<double>> L(n, std::vector<double>(n, 0.0));

    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j <= i; ++j) {
            double sum = 0.0;
            for (size_t k = 0; k < j; ++k) {
                sum += L[i][k] * L[j][k];
            }
            if (i == j) {
                double val = A[i][i] - sum;
                if (val <= 0.0) throw std::runtime_error("Matrix not positive definite");
                L[i][j] = std::sqrt(val);
            } else {
                L[i][j] = (A[i][j] - sum) / L[j][j];
            }
        }
    }
    return L;
}

} // namespace NumericalRecipes
