"""Rosenstein Algorithm for Maximum Lyapunov Exponent from Single Time Series."""
import numpy as np


def estimate_max_lyapunov_divergence(traj: np.ndarray, max_t: int = 10) -> np.ndarray:
    """Compute average logarithmic divergence of nearest neighbors."""
    n = len(traj)
    div = np.zeros(max_t)
    count = 0
    valid_range = n - max_t
    for i in range(valid_range):
        dists = np.linalg.norm(traj[:valid_range] - traj[i], axis=1)
        dists[abs(np.arange(valid_range) - i) < 5] = np.inf
        nn = np.argmin(dists)
        if np.isinf(dists[nn]):
            continue
        d0 = dists[nn]
        for t in range(max_t):
            dt = np.linalg.norm(traj[i + t] - traj[nn + t])
            if dt > 0 and d0 > 0:
                div[t] += np.log(dt / d0)
        count += 1
    return div / max(1, count)
