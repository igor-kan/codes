import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from rayleigh_benard_convection import rayleigh_number, is_convection_unstable

def test_rayleigh_criterion():
    Ra = rayleigh_number(9.81, 1e-3, 10.0, 0.1, 1e-6, 1e-7)
    assert is_convection_unstable(Ra)
