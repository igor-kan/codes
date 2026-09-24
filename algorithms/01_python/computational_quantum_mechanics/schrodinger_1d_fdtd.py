"""Time-Dependent Schrodinger Equation (TDSE) via Split-Operator FFT.

i * hbar * d(psi)/dt = (-hbar^2 / (2m) * d^2/dx^2 + V(x)) psi.
Split-operator method: psi(t + dt) = exp(-i V dt / (2 hbar)) * IFFT[ exp(-i T dt / hbar) * FFT[ exp(-i V dt / (2 hbar)) psi(t) ] ].
"""
import numpy as np


def split_operator_step(psi: np.ndarray, V: np.ndarray, dx: float, dt: float,
                        hbar: float = 1.0, mass: float = 1.0) -> np.ndarray:
    """Perform a single unitary split-operator time step on 1D wave packet."""
    n = len(psi)
    k = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    T_k = (hbar**2 * k**2) / (2.0 * mass)

    half_V_phase = np.exp(-1j * V * dt / (2.0 * hbar))
    T_phase = np.exp(-1j * T_k * dt / hbar)

    psi_half = psi * half_V_phase
    psi_k = np.fft.fft(psi_half)
    psi_k_prop = psi_k * T_phase
    psi_drift = np.fft.ifft(psi_k_prop)
    return psi_drift * half_V_phase
