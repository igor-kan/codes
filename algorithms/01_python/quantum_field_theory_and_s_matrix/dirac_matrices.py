"""Dirac Gamma Matrices in Dirac-Pauli, Weyl (chiral), and Majorana representations.

Satisfies Clifford algebra: {gamma^mu, gamma^nu} = 2 * eta^(mu,nu) * I_4
Metric convention: eta = diag(+1, -1, -1, -1).
"""
import numpy as np
from typing import Dict, Tuple

ETA = np.diag([1.0, -1.0, -1.0, -1.0])

# Pauli matrices
SIGMA_0 = np.eye(2, dtype=complex)
SIGMA_1 = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_3 = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [SIGMA_0, SIGMA_1, SIGMA_2, SIGMA_3]


def get_dirac_pauli_matrices() -> Dict[str, np.ndarray]:
    """Standard Dirac-Pauli representation."""
    gamma0 = np.block([[SIGMA_0, np.zeros((2, 2), dtype=complex)],
                       [np.zeros((2, 2), dtype=complex), -SIGMA_0]])
    gamma1 = np.block([[np.zeros((2, 2), dtype=complex), SIGMA_1],
                       [-SIGMA_1, np.zeros((2, 2), dtype=complex)]])
    gamma2 = np.block([[np.zeros((2, 2), dtype=complex), SIGMA_2],
                       [-SIGMA_2, np.zeros((2, 2), dtype=complex)]])
    gamma3 = np.block([[np.zeros((2, 2), dtype=complex), SIGMA_3],
                       [-SIGMA_3, np.zeros((2, 2), dtype=complex)]])
    gamma5 = 1j * (gamma0 @ gamma1 @ gamma2 @ gamma3)
    return {"g0": gamma0, "g1": gamma1, "g2": gamma2, "g3": gamma3, "g5": gamma5}


def get_weyl_matrices() -> Dict[str, np.ndarray]:
    """Chiral (Weyl) representation."""
    gamma0 = np.block([[np.zeros((2, 2), dtype=complex), SIGMA_0],
                       [SIGMA_0, np.zeros((2, 2), dtype=complex)]])
    gamma1 = np.block([[np.zeros((2, 2), dtype=complex), SIGMA_1],
                       [-SIGMA_1, np.zeros((2, 2), dtype=complex)]])
    gamma2 = np.block([[np.zeros((2, 2), dtype=complex), SIGMA_2],
                       [-SIGMA_2, np.zeros((2, 2), dtype=complex)]])
    gamma3 = np.block([[np.zeros((2, 2), dtype=complex), SIGMA_3],
                       [-SIGMA_3, np.zeros((2, 2), dtype=complex)]])
    gamma5 = 1j * (gamma0 @ gamma1 @ gamma2 @ gamma3)
    return {"g0": gamma0, "g1": gamma1, "g2": gamma2, "g3": gamma3, "g5": gamma5}


def verify_clifford_algebra(gammas: Dict[str, np.ndarray]) -> bool:
    """Verify {gamma^mu, gamma^nu} = 2 * eta^(mu,nu) * I_4."""
    keys = ["g0", "g1", "g2", "g3"]
    I4 = np.eye(4, dtype=complex)
    for mu in range(4):
        for nu in range(4):
            anti_comm = gammas[keys[mu]] @ gammas[keys[nu]] + gammas[keys[nu]] @ gammas[keys[mu]]
            expected = 2.0 * ETA[mu, nu] * I4
            if not np.allclose(anti_comm, expected, atol=1e-12):
                return False
    return True
