"""
Fractional Brownian Motion (fBm) via Davies-Harte Method.
References: Gershenfeld; Evans & Rosenthal.
"""
import numpy as np

def fractional_brownian_motion_circulant(n: int, H: float) -> np.ndarray:
    """Generate fBm sequence of length n with Hurst parameter H using Davies-Harte method."""
    # Autocovariance sequence gamma_k
    k = np.arange(n)
    gamma = 0.5 * (np.abs(k - 1)**(2.0 * H) - 2.0 * (k**(2.0 * H)) + (k + 1)**(2.0 * H))
    gamma[0] = 1.0

    # Embed in circulant vector of length 2(n-1)
    circ = np.concatenate([gamma, gamma[-2:0:-1]])
    eigenvals = np.fft.fft(circ).real
    eigenvals = np.maximum(0.0, eigenvals)

    # Generate complex Gaussian noise
    m = len(circ)
    w = np.random.normal(size=m) + 1j * np.random.normal(size=m)
    f_noise = np.fft.ifft(np.sqrt(eigenvals) * w).real * np.sqrt(m)
    
    # Cumulative sum to obtain fBm
    increments = f_noise[:n]
    return np.cumsum(increments)
