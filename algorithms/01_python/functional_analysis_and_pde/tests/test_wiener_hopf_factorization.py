import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from wiener_hopf_factorization import decompose_analytic_halfplanes

def test_decomposition_sum():
    t = np.linspace(-10, 10, 256)
    f = 1.0 / (1.0 + t**2)
    f_p, f_m = decompose_analytic_halfplanes(f)
    assert np.allclose(f_p + f_m, f)
