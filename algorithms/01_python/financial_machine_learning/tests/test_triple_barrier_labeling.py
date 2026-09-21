import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from triple_barrier_labeling import apply_triple_barrier

def test_barriers():
    # Surges immediately
    prices = np.array([100.0, 103.0, 104.0, 102.0])
    lbl = apply_triple_barrier(prices, upper_factor=0.02, lower_factor=0.02, max_holding=3)
    assert lbl[0] == 1
