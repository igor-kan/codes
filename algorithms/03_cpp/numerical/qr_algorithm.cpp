// QR algorithm for eigenvalues (Numerical Recipes 11.3).
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

void qrDecomposition(const std::vector<std::vector<double>> &matrix,
                     std::vector<std::vector<double>> &q, std::vector<std::vector<double>> &r) {
    int n = static_cast<int>(matrix.size());
    q.assign(n, std::vector<double>(n, 0.0));
    r.assign(n, std::vector<double>(n, 0.0));
    for (int j = 0; j < n; ++j) {
        std::vector<double> v(n);
        for (int i = 0; i < n; ++i) v[i] = matrix[i][j];
        for (int i = 0; i < j; ++i) {
            for (int k = 0; k < n; ++k) r[i][j] += q[k][i] * v[k];
            for (int k = 0; k < n; ++k) v[k] -= r[i][j] * q[k][i];
        }
        double norm = 0.0;
        for (double value : v) norm += value * value;
        r[j][j] = std::sqrt(norm);
        for (int k = 0; k < n; ++k) q[k][j] = v[k] / r[j][j];
    }
}

std::vector<double> qrAlgorithm(std::vector<std::vector<double>> matrix, int iterations = 1000) {
    int n = static_cast<int>(matrix.size());
    for (int iteration = 0; iteration < iterations; ++iteration) {
        std::vector<std::vector<double>> q, r;
        qrDecomposition(matrix, q, r);
        std::vector<std::vector<double>> next(n, std::vector<double>(n, 0.0));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                for (int k = 0; k < n; ++k) next[i][j] += r[i][k] * q[k][j];
        matrix = next;
    }
    std::vector<double> eigenvalues(n);
    for (int i = 0; i < n; ++i) eigenvalues[i] = matrix[i][i];
    std::sort(eigenvalues.begin(), eigenvalues.end());
    return eigenvalues;
}

int main() {
    auto eigenvalues = qrAlgorithm({{2, 1}, {1, 2}});
    assert(std::abs(eigenvalues[0] - 1.0) < 1e-6 && std::abs(eigenvalues[1] - 3.0) < 1e-6);
    std::cout << "qr algorithm ok\n";
    return 0;
}
