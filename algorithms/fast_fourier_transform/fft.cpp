#include <iostream>
#include <vector>
#include <complex>
#include <cmath>
#include <cassert>

using Complex = std::complex<double>;
const double PI = std::acos(-1.0);

// Bit-reversal permutation
void bit_reverse_copy(std::vector<Complex>& a) {
    size_t n = a.size();
    for (size_t i = 1, j = 0; i < n; ++i) {
        size_t bit = n >> 1;
        for (; j & bit; bit >>= 1) {
            j ^= bit;
        }
        j ^= bit;
        if (i < j) {
            std::swap(a[i], a[j]);
        }
    }
}

// In-place Radix-2 Cooley-Tukey FFT
void fft(std::vector<Complex>& a, bool invert = false) {
    size_t n = a.size();
    assert((n & (n - 1)) == 0 && "Array length must be a power of 2");

    bit_reverse_copy(a);

    for (size_t len = 2; len <= n; len <<= 1) {
        double angle = 2 * PI / len * (invert ? -1 : 1);
        Complex wlen(std::cos(angle), std::sin(angle));
        for (size_t i = 0; i < n; i += len) {
            Complex w(1);
            for (size_t j = 0; j < len / 2; ++j) {
                Complex u = a[i + j];
                Complex v = a[i + j + len / 2] * w;
                a[i + j] = u + v;
                a[i + j + len / 2] = u - v;
                w *= wlen;
            }
        }
    }

    if (invert) {
        for (Complex& x : a) {
            x /= n;
        }
    }
}

int main() {
    std::vector<Complex> signal = {1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0};
    std::vector<Complex> copy = signal;

    fft(signal, false);
    fft(signal, true);

    for (size_t i = 0; i < signal.size(); ++i) {
        assert(std::abs(signal[i] - copy[i]) < 1e-10);
    }
    std::cout << "[C++ FFT] In-place forward and inverse FFT validated." << std::endl;
    return 0;
}
