import cmath
import math
from typing import List


def fft_recursive(x: List[complex]) -> List[complex]:
    """Cooley-Tukey Radix-2 Recursive FFT."""
    n = len(x)
    if n <= 1:
        return x
    even = fft_recursive(x[0::2])
    odd = fft_recursive(x[1::2])
    t = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + t[k] for k in range(n // 2)] + [even[k] - t[k] for k in range(n // 2)]


def ifft_recursive(x: List[complex]) -> List[complex]:
    """Inverse Fast Fourier Transform."""
    n = len(x)
    conjugate = [val.conjugate() for val in x]
    transformed = fft_recursive(conjugate)
    return [val.conjugate() / n for val in transformed]


if __name__ == "__main__":
    signal = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    freq = fft_recursive([complex(v) for v in signal])
    recovered = ifft_recursive(freq)

    for orig, rec in zip(signal, recovered):
        assert abs(orig - rec.real) < 1e-10
    print("[Python FFT] Recursive Cooley-Tukey FFT & IFFT validated.")
