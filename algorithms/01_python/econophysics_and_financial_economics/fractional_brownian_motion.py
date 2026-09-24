"""Fractional Brownian Motion (fBm) via Davies-Harte Circulant Matrix Embedding.

Hurst exponent H in (0, 1):
H = 0.5: Standard Brownian motion.
H > 0.5: Persistent (trending) memory.
H < 0.5: Anti-persistent (mean-reverting).
"""
import numpy as np


def autocovariance_fbm(H: float, n: int) -> np.ndarray:
    """Autocovariance gamma(k) = 0.5 * (|k-1|^(2H) - 2|k|^(2H) + |k+1|^(2H))."""
    k = np.arange(n)
    return 0.5 * (np.abs(k - 1)**(2 * H) - 2.0 * np.abs(k)**(2 * H) + np.abs(k + 1)**(2 * H))


def generate_fractional_gaussian_noise(H: float, n: int, seed: int = 42) -> np.ndarray:
    """Generate exact discrete fractional Gaussian noise using spectral embedding."""
    np.random.seed(seed)
    gamma = autocovariance_fbm(H, n)
    c = np.concatenate([gamma, gamma[-2:0:-1]])
    eigenvals = np.real(np.fft.fft(c))
    eigenvals = np.maximum(eigenvals, 0.0)
    
    m = len(c)
    w = np.random.standard_normal(m) + 1j * np.random.standard_normal(m)
    z = np.fft.ifft(np.sqrt(eigenvals) * w)
    return np.real(z[:n]) * np.sqrt(m)
