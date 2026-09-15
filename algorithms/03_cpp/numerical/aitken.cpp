#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

double aitken(double x0, double x1, double x2) {
    double denominator = x2 - 2 * x1 + x0;
    if (std::abs(denominator) < 1e-15) return x2;
    return x2 - (x2 - x1) * (x2 - x1) / denominator;
}

int main() {
    assert(std::abs(aitken(1.0, 0.5, 0.25)) < 1e-12);
    std::vector<double> sequence;
    for (int n = 0; n < 3; ++n) sequence.push_back(2.0 - 2.0 * std::pow(0.5, n));
    assert(std::abs(aitken(sequence[0], sequence[1], sequence[2]) - 2.0) < 1e-12);
    std::cout << "aitken ok\n";
    return 0;
}
