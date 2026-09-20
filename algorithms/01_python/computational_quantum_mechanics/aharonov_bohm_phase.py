"""
Aharonov-Bohm Phase and Vector Potential Accumulation.
References: Landau & Lifshitz - Quantum Mechanics.
"""
import numpy as np

def aharonov_bohm_phase_shift(flux: float, q: float = 1.0, hbar: float = 1.0) -> float:
    """Phase shift Delta phi = (q / hbar) Phi_B."""
    return (q / hbar) * flux

def magnetic_flux_quantum(q: float = 1.0, hbar: float = 1.0) -> float:
    """Flux quantum Phi_0 = 2 pi hbar / q."""
    return 2.0 * np.pi * hbar / q
