import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from correlation_dimension_grassberger_procaccia import correlation_sum

def test_correlation_monotonicity():
    pts = np.random.rand(50, 2)
    c1 = correlation_sum(pts, 0.1)
    c2 = correlation_sum(pts, 0.5)
    assert c1 <= c2
