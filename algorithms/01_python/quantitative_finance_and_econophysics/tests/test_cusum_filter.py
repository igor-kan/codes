import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cusum_filter import cusum_filter_events

def test_cusum_trigger():
    returns = np.array([0.01, 0.02, 0.03, 0.00, -0.05])
    events = cusum_filter_events(returns, threshold=0.04)
    assert 2 in events or 4 in events
