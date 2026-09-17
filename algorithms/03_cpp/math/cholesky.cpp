/**
 * Cholesky LL^T Decomposition in C++ (Numerical Recipes 3rd Ed. Chapter 2.6)
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>

std::vector<std::vector<double>> cholesky(const std::vector<std::vector<double>>& A) {
    int n = A.size();
    std::vector<std::vector<double>> L(n, std::vector<double>(n, 0.0));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            double sum = 0.0;
            for (int k = 0; k < j; k++) sum += L[i][k] * L[j][k];
            if (i == j) {
                double val = A[i][i] - sum;
                assert(val > 0);
                L[i][j] = std::sqrt(val);
            } else {
                L[i][j] = (A[i][j] - sum) / L[j][j];
            }
        }
    }
    return L;
}

int main() {
    std::vector<std::vector<double>> A = {
        {4.0, 12.0, -16.0},
        {12.0, 37.0, -43.0},
        {-16.0, -43.0, 98.0}
    };
    auto L = cholesky(A);
    assert(std::abs(L[0][0] - 2.0) < 1e-6);
    std::cout << "C++ Cholesky Decomposition verified.\n";
    return 0;
}
