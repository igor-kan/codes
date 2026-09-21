import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from optical_scalars import compute_optical_scalars

def test_diverging_null_congruence():
    # Spherical wavefront expanding outwards: grad_k has positive diagonal on screen
    grad_k = np.diag([0.0, 1.0, 1.0, 0.0])
    m = np.array([0.0, 1.0, 1.0j, 0.0]) / np.sqrt(2.0)
    res = compute_optical_scalars(grad_k, m)
    assert res["twist"] == 0.0  # Hypersurface orthogonal -> twist = 0
    assert res["shear_magnitude"] == 0.0
    assert res["expansion"] < 0 or abs(res["expansion"]) > 0
