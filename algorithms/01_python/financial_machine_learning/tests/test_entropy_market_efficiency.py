import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from entropy_market_efficiency import shannon_entropy

def test_entropy():
    # Maximum entropy for fair binary stream
    s = "01010101"
    assert np.isclose(shannon_entropy(s), 1.0)
    # Zero entropy for constant stream
    assert np.isclose(shannon_entropy("000000"), 0.0)
