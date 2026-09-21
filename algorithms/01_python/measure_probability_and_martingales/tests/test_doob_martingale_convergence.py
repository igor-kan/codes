import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from doob_martingale_convergence import count_upcrossings

def test_upcrossings():
    # Sequence dips below 0 and rises above 2 twice
    seq = np.array([1.0, -0.5, 2.5, 0.5, -0.2, 3.0, 1.0])
    u = count_upcrossings(seq, a=0.0, b=2.0)
    assert u == 2
