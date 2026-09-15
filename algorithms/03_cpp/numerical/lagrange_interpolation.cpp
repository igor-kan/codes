// Lagrange polynomial interpolation (Numerical Recipes 3.1).
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

double lagrange(const std::vector<double> &xs, const std::vector<double> &ys, double x) {
    double total = 0.0;
    int n = static_cast<int>(xs.size());
    for (int i = 0; i < n; ++i) {
        double term = ys[i];
        for (int j = 0; j < n; ++j)
            if (i != j) term *= (x - xs[j]) / (xs[i] - xs[j]);
        total += term;
    }
    return total;
}

int main() {
    assert(std::abs(lagrange({0, 1, 2}, {1, 3, 2}, 1.5) - 2.875) < 1e-9);
    std::cout << "lagrange interpolation ok\n";
    return 0;
}
