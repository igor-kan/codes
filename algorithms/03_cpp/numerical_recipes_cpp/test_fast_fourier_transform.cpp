#include "fast_fourier_transform.hpp"
#include <cassert>
#include <cmath>
#include <iostream>

int main() {
    using Complex = NumericalRecipes::Complex;
    std::vector<Complex> signal{1.0, 2.0, 3.0, 4.0, 0.0, 0.0, 0.0, 0.0};
    auto orig = signal;
    NumericalRecipes::fft(signal, false);
    NumericalRecipes::fft(signal, true);
    for (size_t i = 0; i < signal.size(); ++i) {
        assert(std::abs(signal[i] - orig[i]) < 1e-10);
    }
    std::cout << "test_fast_fourier_transform passed\n";
    return 0;
}
