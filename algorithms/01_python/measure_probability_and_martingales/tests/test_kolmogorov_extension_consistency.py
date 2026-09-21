import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kolmogorov_extension_consistency import check_chapman_kolmogorov

def test_semigroup():
    P = np.array([[0.7, 0.3], [0.4, 0.6]])
    P2 = P @ P
    assert check_chapman_kolmogorov(P, P, P2)
