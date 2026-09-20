import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kohn_sham_1d import lda_exchange_potential_1d, hartree_potential_1d

def test_hartree_positive_density():
    x = np.linspace(-5, 5, 100)
    n = np.exp(-x**2)
    v_h = hartree_potential_1d(n, x)
    assert np.all(v_h > 0.0)
