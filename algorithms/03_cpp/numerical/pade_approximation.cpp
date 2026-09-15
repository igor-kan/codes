// Pade approximation from a Taylor series (Numerical Recipes 5.12).
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

std::vector<double> solve(std::vector<std::vector<double>> a, std::vector<double> b) {
    int n = static_cast<int>(b.size());
    for (int col = 0; col < n; ++col) {
        int pivot = col;
        for (int r = col + 1; r < n; ++r) if (std::abs(a[r][col]) > std::abs(a[pivot][col])) pivot = r;
        std::swap(a[col], a[pivot]);
        std::swap(b[col], b[pivot]);
        for (int r = col + 1; r < n; ++r) {
            double factor = a[r][col] / a[col][col];
            for (int k = col; k < n; ++k) a[r][k] -= factor * a[col][k];
            b[r] -= factor * b[col];
        }
    }
    std::vector<double> x(n);
    for (int r = n - 1; r >= 0; --r) {
        double s = b[r];
        for (int k = r + 1; k < n; ++k) s -= a[r][k] * x[k];
        x[r] = s / a[r][r];
    }
    return x;
}

int main() {
    std::vector<double> series{1.0, 1.0, 0.5, 1.0 / 6, 1.0 / 24};
    int l = 2, m = 2;
    std::vector<std::vector<double>> matrix(m, std::vector<double>(m));
    std::vector<double> rhs(m);
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= m; ++j) matrix[i - 1][j - 1] = series[l + i - j];
        rhs[i - 1] = -series[l + i];
    }
    auto q = solve(matrix, rhs);
    std::vector<double> p(l + 1, 0.0);
    for (int i = 0; i <= l; ++i) {
        p[i] = series[i];
        for (int j = 1; j <= std::min(i, m); ++j) p[i] += q[j - 1] * series[i - j];
    }
    double num = 0.0, den = 1.0;
    for (int i = l; i >= 0; --i) num = num * 1.0 + p[i];
    for (int i = m - 1; i >= 0; --i) den = den * 1.0 + q[i];
    assert(std::abs(num / den - 19.0 / 7.0) < 1e-9);
    std::cout << "pade approximation ok\n";
    return 0;
}
