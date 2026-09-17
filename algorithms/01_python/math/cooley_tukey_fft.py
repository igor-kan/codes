"""
Cooley-Tukey FFT in Python (CLRS 3rd Ed. Chapter 30.2).
"""

import cmath

def fft(a, invert=False):
    n = len(a)
    if n == 1:
        return [a[0]]

    a0 = fft(a[0::2], invert)
    a1 = fft(a[1::2], invert)

    angle = (-2 if invert else 2) * cmath.pi / n
    w = 1.0
    wn = cmath.exp(angle * 1j)

    y = [0] * n
    for k in range(n // 2):
        term = w * a1[k]
        y[k] = a0[k] + term
        y[k + n // 2] = a0[k] - term
        if invert:
            y[k] /= 2
            y[k + n // 2] /= 2
        w *= wn
    return y

if __name__ == "__main__":
    sig = [1, 2, 3, 4]
    freq = fft(sig)
    rec = fft(freq, invert=True)
    assert abs(rec[0].real - 1.0) < 1e-6
    print("Python FFT verified.")
