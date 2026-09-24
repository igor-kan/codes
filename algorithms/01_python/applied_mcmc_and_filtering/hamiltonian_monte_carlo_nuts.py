"""Hamiltonian Monte Carlo (HMC) with Symplectic Leapfrog Integrator."""
import numpy as np
from typing import Callable, Tuple


def leapfrog_step(q: np.ndarray, p: np.ndarray, grad_U: Callable, eps: float, L: int) -> Tuple[np.ndarray, np.ndarray]:
    """Perform L symplectic leapfrog steps on position q and momentum p."""
    p = p - 0.5 * eps * grad_U(q)
    for i in range(L):
        q = q + eps * p
        if i != L - 1:
            p = p - eps * grad_U(q)
    p = p - 0.5 * eps * grad_U(q)
    return q, -p


def hmc_sample_step(q_curr: np.ndarray, U: Callable, grad_U: Callable, eps: float = 0.1, L: int = 10) -> np.ndarray:
    """Single HMC transition with Metropolis accept/reject."""
    p_curr = np.random.standard_normal(q_curr.shape)
    q_prop, p_prop = leapfrog_step(q_curr, p_curr, grad_U, eps, L)
    
    H_curr = U(q_curr) + 0.5 * np.sum(p_curr**2)
    H_prop = U(q_prop) + 0.5 * np.sum(p_prop**2)
    
    if np.random.rand() < np.exp(H_curr - H_prop):
        return q_prop
    return q_curr
