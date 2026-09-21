import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hohmann_transfer import hohmann_delta_v

def test_zero_transfer():
    dv1, dv2, tot = hohmann_delta_v(1.0, 1.0)
    assert tot == 0.0
