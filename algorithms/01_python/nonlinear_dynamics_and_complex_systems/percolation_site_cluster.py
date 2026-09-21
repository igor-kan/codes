"""
Site Percolation and Spanning Cluster Verification on 2D Square Lattice.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 15; Stauffer, Introduction to Percolation Theory.
"""
import numpy as np

def has_percolating_cluster_top_bottom(grid: np.ndarray) -> bool:
    """Checks if there is a connected path of occupied sites from top to bottom."""
    n_rows, n_cols = grid.shape
    visited = np.zeros_like(grid, dtype=bool)
    stack = [(0, c) for c in range(n_cols) if grid[0, c] == 1]
    
    for r, c in stack:
        visited[r, c] = True
        
    while stack:
        r, c = stack.pop()
        if r == n_rows - 1:
            return True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n_rows and 0 <= nc < n_cols:
                if grid[nr, nc] == 1 and not visited[nr, nc]:
                    visited[nr, nc] = True
                    stack.append((nr, nc))
    return False
