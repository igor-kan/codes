import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sandpile_bak_tang_wiesenfeld import relax_sandpile

def test_sandpile():
    grid = np.zeros((3, 3), dtype=int)
    grid[1, 1] = 4
    topples = relax_sandpile(grid)
    assert topples == 1
    assert grid[1, 1] == 0
    assert grid[0, 1] == 1
