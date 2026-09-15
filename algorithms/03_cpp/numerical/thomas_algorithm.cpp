#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

std::vector<double> thomasAlgorithm(const std::vector<double> &lower, const std::vector<double> &diagonal,
                                    const std::vector<double> &upper, const std::vector<double> &rhs) {
    int n = static_cast<int>(diagonal.size());
    std::vector<double> c(n), d(n), x(n);
    c[0] = upper[0] / diagonal[0];
    d[0] = rhs[0] / diagonal[0];
    for (int i = 1; i < n; ++i) {
        double denominator = diagonal[i] - lower[i] * c[i - 1];
        c[i] = (i < n - 1) ? upper[i] / denominator : 0.0;
        d[i] = (rhs[i] - lower[i] * d[i - 1]) / denominator;
    }
    x[n - 1] = d[n - 1];
    for (int i = n - 2; i >= 0; --i) x[i] = d[i] - c[i] * x[i + 1];
    return x;
}

int main() {
    auto x = thomasAlgorithm({0, -1, -1}, {2, 2, 2}, {-1, -1, 0}, {1, 0, 1});
    for (double value : x) assert(std::abs(value - 1.0) < 1e-12);
    std::cout << "thomas algorithm ok\n";
    return 0;
}
