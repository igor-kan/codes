import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from triple_barrier_labeling import apply_triple_barrier

def test_profit_hit():
    prices = np.array([100.0, 101.0, 103.0, 100.0, 99.0])
    labels = apply_triple_barrier(prices, pt_mult=1.0, sl_mult=1.0, max_holding=3, vol=0.02)
    # At index 0, upper barrier is 102. Price reaches 103 at step 2 -> label +1
    assert labels[0] == 1
