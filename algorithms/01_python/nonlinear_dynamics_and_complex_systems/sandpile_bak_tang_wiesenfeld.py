"""
Bak-Tang-Wiesenfeld (BTW) Abelian Sandpile Self-Organized Criticality Model.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 15; Bak et al. (1987).
"""
import numpy as np

def relax_sandpile(grid: np.ndarray) -> int:
    """Topples all sites with grains >= 4 until stable. Returns total avalanche size."""
    topples = 0
    n, m = grid.shape
    while True:
        unstable = np.argwhere(grid >= 4)
        if len(unstable) == 0:
            break
        for r, c in unstable:
            grid[r, c] -= 4
            topples += 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    grid[nr, nc] += 1
    return topples
