"""
Frobenius Theorem: Integrability criterion for 1-forms and distributions.
Reference: Penrose, The Road to Reality, Ch. 14.
"""
import numpy as np

def frobenius_involutive_check(bracket_matrix: np.ndarray, distribution_basis: np.ndarray) -> bool:
    """
    Checks if the Lie bracket of basis vector fields lies in the linear span of the distribution.
    [X_i, X_j] in span(X_1, ..., X_k).
    """
    # Project bracket onto orthogonal complement of distribution
    Q, R = np.linalg.qr(distribution_basis.T)
    # Residual projection
    residual = bracket_matrix - Q @ (Q.T @ bracket_matrix)
    return bool(np.allclose(residual, 0.0, atol=1e-6))
