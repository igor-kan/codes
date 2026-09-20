import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from calmar_and_drawdown import max_drawdown

def test_drawdown():
    curve = np.array([100.0, 120.0, 90.0, 110.0])
    # Peak is 120, trough is 90 -> drawdown is (120-90)/120 = 25%
    mdd = max_drawdown(curve)
    assert np.isclose(mdd, 0.25)
