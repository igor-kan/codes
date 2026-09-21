import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from raychaudhuri_equation import raychaudhuri_null_derivative

def test_focusing_theorem():
    # Without twist (omega=0) and non-negative Ricci curvature, dtheta/dlambda <= 0 (gravitational focusing)
    dtheta = raychaudhuri_null_derivative(theta=1.0, shear_sq=0.1, twist_sq=0.0, ricci_null_contraction=0.5)
    assert dtheta < 0.0
