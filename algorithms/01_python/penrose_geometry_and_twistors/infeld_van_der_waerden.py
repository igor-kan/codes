"""
Infeld-van der Waerden symbols connecting 4-vectors to Hermitian 2x2 matrices.
Reference: Penrose, The Road to Reality, Ch. 22.
"""
import numpy as np

SIGMA_MU = [
    np.array([[1.0, 0.0], [0.0, 1.0]], dtype=complex) / np.sqrt(2.0),
    np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex) / np.sqrt(2.0),
    np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex) / np.sqrt(2.0),
    np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex) / np.sqrt(2.0),
]

def four_vector_to_spinor_matrix(v: np.ndarray) -> np.ndarray:
    """
    Maps 4-vector v^mu to Hermitian 2x2 matrix P_{AB'} = v^mu sigma_mu_{AB'}.
    """
    P = np.zeros((2, 2), dtype=complex)
    for mu in range(4):
        P += v[mu] * SIGMA_MU[mu]
    return P

def spinor_matrix_to_four_vector(P: np.ndarray) -> np.ndarray:
    """
    Inverts the mapping: v_mu = Tr(P sigma_mu).
    """
    v = np.zeros(4, dtype=float)
    for mu in range(4):
        v[mu] = np.trace(P @ SIGMA_MU[mu]).real
    return v
