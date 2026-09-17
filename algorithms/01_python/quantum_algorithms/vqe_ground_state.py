"""Variational Quantum Eigensolver (VQE) for Ground State Energies.

Optimizes parameterized ansatz |psi(theta)> to minimize expectation value <psi(theta)| H |psi(theta)>.
"""

from typing import Callable, Sequence, Tuple
import numpy as np
from scipy.optimize import minimize


class VQESolver:
    """Variational Quantum Eigensolver simulator."""

    def __init__(self, hamiltonian_matrix: np.ndarray):
        self.h = np.array(hamiltonian_matrix, dtype=np.complex128)
        self.dim = self.h.shape[0]

    def energy_expectation(self, state: np.ndarray) -> float:
        """<psi| H |psi>."""
        s = np.array(state, dtype=np.complex128)
        norm = np.linalg.norm(s)
        s = s / norm
        return float(np.real(s.conj() @ self.h @ s))

    def solve_2level_ansatz(self) -> Tuple[float, float]:
        """Parameterized state |psi(theta)> = cos(theta)|0> + sin(theta)|1>."""
        def loss(theta):
            th = theta[0]
            psi = np.array([np.cos(th), np.sin(th)])
            return self.energy_expectation(psi)

        res = minimize(loss, [0.0], method='BFGS')
        exact_e0 = float(np.min(np.linalg.eigvalsh(self.h)))
        return float(res.fun), exact_e0
