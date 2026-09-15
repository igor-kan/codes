// Power iteration for the dominant eigenvalue (Numerical Recipes 11.1).
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

double powerMethod(const std::vector<std::vector<double>> &matrix, std::vector<double> &vector) {
    int n = static_cast<int>(matrix.size());
    vector.assign(n, 1.0);
    double eigenvalue = 0.0;
    for (int iteration = 0; iteration < 1000; ++iteration) {
        std::vector<double> product(n, 0.0);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) product[i] += matrix[i][j] * vector[j];
        double norm = 0.0;
        for (double value : product) norm = std::max(norm, std::abs(value));
        for (int i = 0; i < n; ++i) vector[i] = product[i] / norm;
        if (std::abs(norm - eigenvalue) < 1e-12) { eigenvalue = norm; break; }
        eigenvalue = norm;
    }
    return eigenvalue;
}

int main() {
    std::vector<std::vector<double>> matrix{{4, 1}, {2, 3}};
    std::vector<double> vector;
    double eigenvalue = powerMethod(matrix, vector);
    assert(std::abs(eigenvalue - 5.0) < 1e-9);
    for (int i = 0; i < 2; ++i) {
        double residual = matrix[i][0] * vector[0] + matrix[i][1] * vector[1] - eigenvalue * vector[i];
        assert(std::abs(residual) < 1e-9);
    }
    std::cout << "power method ok\n";
    return 0;
}
