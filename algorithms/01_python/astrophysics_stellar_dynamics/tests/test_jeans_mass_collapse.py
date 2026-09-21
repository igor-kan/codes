import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from jeans_mass_collapse import jeans_length, jeans_mass

def test_jeans_positive():
    lam = jeans_length(10.0, 1e-18)
    M = jeans_mass(10.0, 1e-18)
    assert lam > 0.0
    assert M > 0.0
