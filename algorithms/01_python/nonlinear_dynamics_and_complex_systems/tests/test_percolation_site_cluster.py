import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from percolation_site_cluster import has_percolating_cluster_top_bottom

def test_percolation():
    # Vertical line percolates
    grid = np.zeros((5, 5), dtype=int)
    grid[:, 2] = 1
    assert has_percolating_cluster_top_bottom(grid)
    # Empty grid does not
    assert not has_percolating_cluster_top_bottom(np.zeros((5, 5), dtype=int))
