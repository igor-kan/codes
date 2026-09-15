#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

std::pair<double, double> leastSquaresLinear(const std::vector<double> &xs, const std::vector<double> &ys) {
    double n = xs.size(), meanX = 0.0, meanY = 0.0;
    for (size_t i = 0; i < xs.size(); ++i) { meanX += xs[i] / n; meanY += ys[i] / n; }
    double numerator = 0.0, denominator = 0.0;
    for (size_t i = 0; i < xs.size(); ++i) {
        numerator += (xs[i] - meanX) * (ys[i] - meanY);
        denominator += (xs[i] - meanX) * (xs[i] - meanX);
    }
    double slope = numerator / denominator;
    return {meanY - slope * meanX, slope};
}

int main() {
    auto [intercept, slope] = leastSquaresLinear({0, 1, 2, 3}, {1, 3, 5, 7});
    assert(std::abs(intercept - 1.0) < 1e-12 && std::abs(slope - 2.0) < 1e-12);
    std::cout << "least squares linear ok\n";
    return 0;
}
