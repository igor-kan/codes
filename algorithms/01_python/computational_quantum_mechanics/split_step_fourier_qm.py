"""Split-Step Fourier Method for Quantum Wavepacket Propagation."""
import numpy as np


def split_step_propagate_1d(psi0: np.ndarray, x: np.ndarray, V: np.ndarray,
                            dt: float, n_steps: int, mass: float = 1.0, hbar: float = 1.0) -> np.ndarray:
    """Propagate wavepacket over n_steps."""
    dx = x[1] - x[0]
    n = len(x)
    k = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    T_k = (hbar**2 * k**2) / (2.0 * mass)

    phase_V = np.exp(-0.5j * V * dt / hbar)
    phase_T = np.exp(-1.0j * T_k * dt / hbar)

    psi = psi0.copy()
    for _ in range(n_steps):
        psi *= phase_V
        psi = np.fft.ifft(np.fft.fft(psi) * phase_T)
        psi *= phase_V
    return psi
