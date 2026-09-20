import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from percolation_2d import check_percolation_2d

def test_percolation_limits():
    np.random.seed(42)
    # p = 0.99 definitely percolates
    assert check_percolation_2d(0.99, 20)
    # p = 0.01 never percolates
    assert not check_percolation_2d(0.01, 20)
