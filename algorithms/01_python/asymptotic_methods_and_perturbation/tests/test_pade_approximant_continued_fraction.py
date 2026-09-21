import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pade_approximant_continued_fraction import pade_11_coefficients, eval_pade_11

def test_exp_pade():
    # e^x approx 1 + x + 1/2 x^2 -> [1/1] = (1 + x/2) / (1 - x/2)
    a0, a1, b1 = pade_11_coefficients(1.0, 1.0, 0.5)
    val = eval_pade_11(0.1, a0, a1, b1)
    assert np.isclose(val, np.exp(0.1), atol=1e-3)
