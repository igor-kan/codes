import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from synthetic_data_copula import sample_gaussian_copula

def test_copula_bounds():
    corr = np.array([[1.0, 0.5], [0.5, 1.0]])
    u = sample_gaussian_copula(corr, 100)
    assert np.all((u >= 0.0) & (u <= 1.0))
