import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lyapunov_exponent_estimation import estimate_1d_lyapunov

def test_logistic_lyapunov():
    # Fully chaotic logistic map r=4.0: lambda = ln(2) approx 0.69315
    f = lambda x: 4.0 * x * (1.0 - x)
    df = lambda x: 4.0 * (1.0 - 2.0 * x)
    l = estimate_1d_lyapunov(f, df, 0.2, n_iterations=3000, n_transient=500)
    assert np.isclose(l, np.log(2.0), atol=0.05)
