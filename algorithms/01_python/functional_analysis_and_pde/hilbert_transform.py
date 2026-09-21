"""
Hilbert Transform and Analytic Signal Representation via FFT.
Reference: Blennow, Mathematical Methods for Physics and Engineering.
"""
import numpy as np

def compute_hilbert_transform(signal: np.ndarray) -> np.ndarray:
    """
    H[u](t) = (1 / pi) P.V. int u(tau)/(t - tau) d tau.
    Multiplies negative frequencies by +i and positive frequencies by -i in Fourier domain.
    """
    N = len(signal)
    F = np.fft.fft(signal)
    h = np.zeros(N)
    if N % 2 == 0:
        h[0] = 1
        h[N//2] = 1
        h[1:N//2] = 2
    else:
        h[0] = 1
        h[1:(N+1)//2] = 2
    # Analytic signal
    analytic = np.fft.ifft(F * h)
    return analytic.imag
