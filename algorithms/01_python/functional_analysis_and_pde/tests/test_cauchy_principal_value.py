import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cauchy_principal_value import cauchy_principal_value_symmetric

def test_odd_pole_cancellation():
    # P.V. int_{-1}^1 1 / x dx = 0
    pv = cauchy_principal_value_symmetric(lambda x: 1.0, 0.0, -1.0, 1.0)
    assert np.isclose(pv, 0.0, atol=1e-4)
