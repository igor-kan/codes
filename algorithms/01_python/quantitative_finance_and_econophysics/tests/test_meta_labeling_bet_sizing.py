import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from meta_labeling_bet_sizing import bet_size_sigmoid

def test_bet_size():
    # p = 0.5 for binary choice gives 0 bet size
    assert np.isclose(bet_size_sigmoid(0.5), 0.0, atol=1e-5)
    # p > 0.5 gives positive bet size
    assert bet_size_sigmoid(0.8) > 0.0
