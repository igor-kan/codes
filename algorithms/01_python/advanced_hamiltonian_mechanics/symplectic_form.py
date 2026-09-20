"""
Canonical Symplectic 2-Form and Symplectic Matrix Verification.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics (Ch. 8).
"""
import numpy as np

def standard_symplectic_matrix(n: int) -> np.ndarray:
    """Construct standard 2n x 2n symplectic matrix J = [[0, I], [-I, 0]]."""
    I = np.eye(n)
    Z = np.zeros((n, n))
    return np.block([[Z, I], [-I, Z]])

def is_symplectic_matrix(M: np.ndarray, tol: float = 1e-10) -> bool:
    """Check if M satisfies M^T J M = J."""
    n2 = M.shape[0]
    n = n2 // 2
    J = standard_symplectic_matrix(n)
    diff = M.T @ J @ M - J
    return bool(np.max(np.abs(diff)) < tol)

def evaluate_symplectic_form(v1: np.ndarray, v2: np.ndarray) -> float:
    """Evaluate omega(v1, v2) = v1^T J v2."""
    n = len(v1) // 2
    J = standard_symplectic_matrix(n)
    return float(v1.T @ J @ v2)
