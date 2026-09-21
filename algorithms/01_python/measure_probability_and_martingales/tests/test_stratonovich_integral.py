import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from stratonovich_integral import stratonovich_integral

def test_stratonovich_w_dw():
    # int_0^T W o dW = 1/2 W(T)^2
    t = np.linspace(0, 1, 1000)
    W = np.sin(t)  # Smooth test path
    res = stratonovich_integral(lambda w: w, W, t)
    expected = 0.5 * (W[-1]**2 - W[0]**2)
    assert np.isclose(res, expected, atol=1e-4)
