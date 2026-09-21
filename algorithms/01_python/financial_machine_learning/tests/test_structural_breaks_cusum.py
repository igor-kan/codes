import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from structural_breaks_cusum import cusum_filter

def test_cusum_filter():
    r = np.array([0.01, 0.01, 0.02, 0.0, -0.05])
    ev = cusum_filter(r, threshold=0.035)
    assert 2 in ev or 4 in ev
