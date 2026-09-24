"""2D Ising Model Metropolis-Hastings Monte Carlo with Periodic Boundary Conditions."""
import numpy as np


def ising_metropolis_step(spins: np.ndarray, beta: float, J: float = 1.0) -> np.ndarray:
    """Perform one full lattice sweep of Metropolis spin-flip proposals."""
    L = spins.shape[0]
    for _ in range(L * L):
        i = np.random.randint(0, L)
        j = np.random.randint(0, L)
        s = spins[i, j]
        # Nearest neighbours with periodic boundaries
        nb = spins[(i + 1) % L, j] + spins[(i - 1) % L, j] + spins[i, (j + 1) % L] + spins[i, (j - 1) % L]
        dE = 2.0 * J * s * nb
        if dE <= 0 or np.random.rand() < np.exp(-beta * dE):
            spins[i, j] = -s
    return spins
