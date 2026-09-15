#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

std::pair<double, std::vector<double>> rayleighQuotient(const std::vector<std::vector<double>> &matrix,
                                                        const std::vector<double> &vector) {
    int n = matrix.size();
    double scale = 0.0;
    for (double value : vector) scale = std::max(scale, std::abs(value));
    std::vector<double> x(n);
    for (int i = 0; i < n; ++i) x[i] = vector[i] / scale;
    double eigenvalue = 0.0;
    for (int iteration = 0; iteration < 100; ++iteration) {
        std::vector<double> product(n, 0.0);
        double norm = 0.0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) product[i] += matrix[i][j] * x[j];
            norm = std::max(norm, std::abs(product[i]));
        }
        for (int i = 0; i < n; ++i) x[i] = product[i] / norm;
        double numerator = 0.0, denominator = 0.0;
        for (int i = 0; i < n; ++i) {
            double ax = 0.0;
            for (int j = 0; j < n; ++j) ax += matrix[i][j] * x[j];
            numerator += x[i] * ax;
            denominator += x[i] * x[i];
        }
        double next = numerator / denominator;
        if (std::abs(next - eigenvalue) < 1e-12) { eigenvalue = next; break; }
        eigenvalue = next;
    }
    return {eigenvalue, x};
}

int main() {
    auto [eigenvalue, vector] = rayleighQuotient({{2, 1}, {1, 2}}, {1, 0});
    assert(std::abs(eigenvalue - 3.0) < 1e-9);
    std::cout << "rayleigh quotient ok\n";
    return 0;
}
