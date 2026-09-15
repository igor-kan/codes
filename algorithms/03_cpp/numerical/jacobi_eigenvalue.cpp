// Jacobi eigenvalue algorithm (Numerical Recipes 11.1).
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

std::vector<double> jacobiEigenvalue(std::vector<std::vector<double>> a,
                                     std::vector<std::vector<double>> &vectors) {
    int n = static_cast<int>(a.size());
    vectors.assign(n, std::vector<double>(n, 0.0));
    for (int i = 0; i < n; ++i) vectors[i][i] = 1.0;
    for (int iteration = 0; iteration < 100; ++iteration) {
        int p = 0, q = 1;
        double largest = 0.0;
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                if (std::abs(a[i][j]) > largest) { largest = std::abs(a[i][j]); p = i; q = j; }
        if (largest < 1e-12) break;
        double theta = 0.5 * std::atan2(2.0 * a[p][q], a[q][q] - a[p][p]);
        double c = std::cos(theta), s = std::sin(theta);
        for (int k = 0; k < n; ++k) {
            double akp = a[k][p], akq = a[k][q];
            a[k][p] = c * akp - s * akq;
            a[k][q] = s * akp + c * akq;
        }
        for (int k = 0; k < n; ++k) {
            double apk = a[p][k], aqk = a[q][k];
            a[p][k] = c * apk - s * aqk;
            a[q][k] = s * apk + c * aqk;
        }
        for (int k = 0; k < n; ++k) {
            double vkp = vectors[k][p], vkq = vectors[k][q];
            vectors[k][p] = c * vkp - s * vkq;
            vectors[k][q] = s * vkp + c * vkq;
        }
    }
    std::vector<double> eigenvalues(n);
    for (int i = 0; i < n; ++i) eigenvalues[i] = a[i][i];
    return eigenvalues;
}

int main() {
    std::vector<std::vector<double>> matrix{{4, 1, 0}, {1, 3, 1}, {0, 1, 2}};
    std::vector<std::vector<double>> vectors;
    auto eigenvalues = jacobiEigenvalue(matrix, vectors);
    double sum = 0.0, product = 1.0;
    for (double value : eigenvalues) { sum += value; product *= value; }
    assert(std::abs(sum - 9.0) < 1e-9 && std::abs(product - 18.0) < 1e-9);
    std::cout << "jacobi eigenvalue ok\n";
    return 0;
}
