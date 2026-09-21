import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bet_sizing_sigmoid import compute_bet_size

def test_bet_size():
    # p = 0.5 (neutral) -> bet size = 0
    assert np.isclose(compute_bet_size(0.5), 0.0)
    # p > 0.5 -> positive bet size
    assert compute_bet_size(0.7) > 0.0
