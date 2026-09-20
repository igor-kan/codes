import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from poynting_flux_integrator import poynting_vector, maxwell_stress_tensor

def test_plane_wave_flux():
    # Plane wave propagating along z: E = (E0, 0, 0), B = (0, B0, 0)
    E = np.array([1.0, 0.0, 0.0])
    B = np.array([0.0, 1.0, 0.0])
    S = poynting_vector(E, B)
    assert np.allclose(S, [0.0, 0.0, 1.0])
    T = maxwell_stress_tensor(E, B)
    # Trace of T for radiation is -u = -(eps0 E^2 + B^2/mu0)/2
    assert np.isclose(np.trace(T), -1.0)
