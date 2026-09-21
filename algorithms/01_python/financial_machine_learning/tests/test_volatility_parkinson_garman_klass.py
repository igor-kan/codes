import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from volatility_parkinson_garman_klass import parkinson_volatility

def test_parkinson():
    h = np.array([102.0, 104.0, 101.0])
    l = np.array([98.0, 99.0, 99.0])
    vol = parkinson_volatility(h, l)
    assert vol > 0.0
