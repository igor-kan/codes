import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from optimal_execution_almgren_chriss import linear_liquidation_trajectory

def test_execution():
    trades = linear_liquidation_trajectory(1000.0, 10)
    assert len(trades) == 10
    assert np.isclose(np.sum(trades), 1000.0)
