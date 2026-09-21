import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from borel_cantelli_simulation import check_borel_cantelli_summability

def test_summability():
    n = np.arange(1, 1000)
    probs = 1.0 / (n**2)
    assert check_borel_cantelli_summability(probs)
