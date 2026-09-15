// Gaussian elimination with partial pivoting.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

int main() {
    std::vector<std::vector<double>> a{{2, 1, -1, 8}, {-3, -1, 2, -11}, {-2, 1, 2, -3}};
    const int n = 3;
    for (int c = 0; c < n; ++c) {
        int p = c;
        for (int r = c + 1; r < n; ++r) if (std::abs(a[r][c]) > std::abs(a[p][c])) p = r;
        std::swap(a[c], a[p]);
        for (int r = c + 1; r < n; ++r) {
            double f = a[r][c] / a[c][c];
            for (int k = c; k <= n; ++k) a[r][k] -= f * a[c][k];
        }
    }
    std::vector<double> x(n);
    for (int r = n - 1; r >= 0; --r) {
        double s = a[r][n];
        for (int k = r + 1; k < n; ++k) s -= a[r][k] * x[k];
        x[r] = s / a[r][r];
    }
    assert(std::abs(x[0] - 2) < 1e-9 && std::abs(x[1] - 3) < 1e-9 && std::abs(x[2] + 1) < 1e-9);
    std::cout << "x=" << x[0] << ' ' << x[1] << ' ' << x[2] << '\n';
    return 0;
}
