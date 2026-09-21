import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from weyl_curvature_decomposition import electric_magnetic_weyl_parts

def test_weyl_electric_trace():
    # For any vacuum or Weyl tensor, the electric part is traceless
    C = np.zeros((4, 4, 4, 4))
    # Fill standard quad for plane wave
    C[0, 1, 0, 1] = 1.0
    C[0, 2, 0, 2] = -1.0
    u = np.array([1.0, 0.0, 0.0, 0.0])
    E_full, E_3d = electric_magnetic_weyl_parts(C, u)
    assert np.isclose(np.trace(E_3d), 0.0)
