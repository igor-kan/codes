"""
Symplectic Reduction of SO(3) and Casimir Invariants on so(3)*.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics (Appendix 2).
"""
import numpy as np

def so3_casimir(L: np.ndarray) -> float:
    """Casimir function C(L) = |L|^2 on the Poisson manifold so(3)*."""
    return float(np.dot(L, L))

def so3_poisson_bracket(f_grad: np.ndarray, g_grad: np.ndarray, L: np.ndarray) -> float:
    """Poisson bracket on so(3)*: {f, g}(L) = -L . (grad f x grad g)."""
    return float(-np.dot(L, np.cross(f_grad, g_grad)))
