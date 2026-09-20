"""
2D Square Lattice Ising Model Simulation via Metropolis Algorithm.
References: Landau & Lifshitz - Statistical Physics (Vol. 5); Gershenfeld.
"""
import numpy as np

def ising_metropolis_sweep(lattice: np.ndarray, beta: float, J: float = 1.0):
    """Perform one full Monte Carlo sweep (L x L single-spin flip attempts)."""
    L = lattice.shape[0]
    for _ in range(L * L):
        i = np.random.randint(0, L)
        j = np.random.randint(0, L)
        s = lattice[i, j]
        # Periodic nearest neighbor sum
        neighbors = (
            lattice[(i + 1) % L, j] + lattice[(i - 1) % L, j] +
            lattice[i, (j + 1) % L] + lattice[i, (j - 1) % L]
        )
        dE = 2.0 * J * s * neighbors
        if dE <= 0 or np.random.uniform(0.0, 1.0) < np.exp(-beta * dE):
            lattice[i, j] = -s
    return lattice

def ising_magnetization(lattice: np.ndarray) -> float:
    """Average magnetization per spin |m|."""
    return float(np.abs(np.mean(lattice)))
