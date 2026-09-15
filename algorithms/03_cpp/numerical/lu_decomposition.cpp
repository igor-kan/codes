// LU decomposition with partial pivoting (Numerical Recipes 2.3).
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

std::vector<double> luSolve(std::vector<std::vector<double>> a, std::vector<double> b) {
    int n = static_cast<int>(a.size());
    for (int col = 0; col < n; ++col) {
        int pivot = col;
        for (int r = col + 1; r < n; ++r)
            if (std::abs(a[r][col]) > std::abs(a[pivot][col])) pivot = r;
        std::swap(a[col], a[pivot]);
        std::swap(b[col], b[pivot]);
        for (int r = col + 1; r < n; ++r) {
            double f = a[r][col] / a[col][col];
            for (int k = col; k < n; ++k) a[r][k] -= f * a[col][k];
            b[r] -= f * b[col];
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
    auto x = luSolve({{2, 1, -1}, {-3, -1, 2}, {-2, 1, 2}}, {8, -11, -3});
    assert(std::abs(x[0] - 2) < 1e-9 && std::abs(x[1] - 3) < 1e-9 && std::abs(x[2] + 1) < 1e-9);
    std::cout << "lu decomposition ok\n";
    return 0;
}
