"""
Total Variation Distance to Stationarity and Markov Chain Mixing Time.
Reference: Evans & Rosenthal; Levin & Peres, Markov Chains and Mixing Times.
"""
import numpy as np

def total_variation_distance(p: np.ndarray, q: np.ndarray) -> float:
    """||p - q||_TV = 1/2 sum_x |p(x) - q(x)|."""
    return float(0.5 * np.sum(np.abs(p - q)))

def compute_mixing_time(transition_matrix: np.ndarray, pi_stationary: np.ndarray,
                        epsilon: float = 0.25, max_steps: int = 1000) -> int:
    """Computes t_mix(epsilon) = min { t : max_x ||P^t(x, .) - pi||_TV <= epsilon }."""
    n = transition_matrix.shape[0]
    Pt = np.eye(n)
    for t in range(1, max_steps + 1):
        Pt = Pt @ transition_matrix
        max_tv = max(total_variation_distance(Pt[i, :], pi_stationary) for i in range(n))
        if max_tv <= epsilon:
            return t
    return max_steps
