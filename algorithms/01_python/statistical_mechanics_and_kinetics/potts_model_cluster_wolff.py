"""Wolff Cluster Monte Carlo Algorithm for q-State Potts Model."""
import numpy as np


def wolff_potts_step(lattice: np.ndarray, q: int, beta: float, J: float = 1.0) -> np.ndarray:
    """Flip a single connected Wolff cluster."""
    L = lattice.shape[0]
    p_add = 1.0 - np.exp(-beta * J)
    i0, j0 = np.random.randint(0, L), np.random.randint(0, L)
    old_state = lattice[i0, j0]
    new_state = np.random.choice([s for s in range(q) if s != old_state])
    
    cluster = [(i0, j0)]
    visited = np.zeros((L, L), dtype=bool)
    visited[i0, j0] = True
    lattice[i0, j0] = new_state
    
    head = 0
    while head < len(cluster):
        ci, cj = cluster[head]
        head += 1
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = (ci + di) % L, (cj + dj) % L
            if not visited[ni, nj] and lattice[ni, nj] == old_state:
                if np.random.rand() < p_add:
                    visited[ni, nj] = True
                    lattice[ni, nj] = new_state
                    cluster.append((ni, nj))
    return lattice
