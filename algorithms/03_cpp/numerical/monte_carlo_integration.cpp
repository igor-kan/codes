#include <algorithm>
#include <cassert>
#include <cmath>
#include <functional>
#include <iostream>
#include <utility>
#include <vector>

double monteCarloIntegration(const std::function<double(double)> &f, double a, double b, int samples) {
    long long state = 42;
    const long long modulus = 1LL << 31;
    double total = 0.0;
    for (int i = 0; i < samples; ++i) {
        state = (1103515245LL * state + 12345) % modulus;
        total += f(a + (b - a) * static_cast<double>(state) / static_cast<double>(modulus));
    }
    return (b - a) * total / samples;
}

int main() {
    assert(std::abs(monteCarloIntegration([](double x) { return x * x; }, 0, 1, 100000) - 1.0 / 3.0) < 0.01);
    std::cout << "monte carlo integration ok\n";
    return 0;
}
