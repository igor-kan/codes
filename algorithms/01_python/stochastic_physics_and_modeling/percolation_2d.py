"""
2D Site Percolation and Hoshen-Kopelman Cluster Search.
References: Gershenfeld - The Nature of Mathematical Modeling.
"""
import numpy as np
from scipy.ndimage import label

def check_percolation_2d(p: float, L: int) -> bool:
    """Generate random site percolation grid of size L x L with occupation prob p, check vertical percolation."""
    grid = np.random.uniform(0.0, 1.0, size=(L, L)) < p
    labeled_grid, num_clusters = label(grid)
    if num_clusters == 0:
        return False
    # Check if any cluster touches both top row and bottom row
    top_labels = set(np.unique(labeled_grid[0, :])) - {0}
    bottom_labels = set(np.unique(labeled_grid[-1, :])) - {0}
    return len(top_labels.intersection(bottom_labels)) > 0
