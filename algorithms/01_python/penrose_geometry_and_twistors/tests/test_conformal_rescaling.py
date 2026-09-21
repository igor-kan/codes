import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from conformal_rescaling import conformally_rescaled_ricci_scalar

def test_4d_conformal_ricci():
    # In 4D, grad_omega_sq does not affect scalar curvature directly
    r1 = conformally_rescaled_ricci_scalar(10.0, 2.0, 1.0, 100.0, dim=4)
    r2 = conformally_rescaled_ricci_scalar(10.0, 2.0, 1.0, 0.0, dim=4)
    assert np.isclose(r1, r2)
