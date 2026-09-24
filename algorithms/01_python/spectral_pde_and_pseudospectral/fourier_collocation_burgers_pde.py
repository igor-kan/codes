"""Viscous Burgers Equation u_t + u * u_x = nu * u_xx via Fourier Collocation."""
import numpy as np


def burgers_spectral_rhs(u: np.ndarray, nu: float, L: float = 2.0 * np.pi) -> np.ndarray:
    """Compute time derivative rhs using pseudospectral 2/3 dealiasing."""
    N = len(u)
    k = np.fft.fftfreq(N, d=L / (2.0 * np.pi * N))
    u_hat = np.fft.fft(u)
    
    # 2/3 dealiasing rule
    cutoff = int(N / 3.0)
    u_hat_dealiased = u_hat.copy()
    u_hat_dealiased[cutoff:N - cutoff] = 0.0
    
    u_x = np.real(np.fft.ifft(1j * k * u_hat_dealiased))
    u_xx = np.real(np.fft.ifft(- (k**2) * u_hat))
    return -u * u_x + nu * u_xx
