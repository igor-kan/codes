import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from conformal_mapping import joukowsky_transform, complex_velocity

def test_joukowsky_circle():
    theta = np.linspace(0, 2*np.pi, 201)
    # Circle of radius 1 maps to flat plate segment [-2, 2]
    z = np.exp(1j * theta)
    w = joukowsky_transform(z, c=1.0)
    assert np.allclose(w.imag, 0.0, atol=1e-12)
    assert np.isclose(np.max(w.real), 2.0, atol=1e-5)
    assert np.isclose(np.min(w.real), -2.0, atol=1e-5)

def test_stagnation_points():
    # Stagnation points for cylinder without circulation are at theta = 0, pi (z = +-R)
    v_stag1 = complex_velocity(1.0, U=1.0, R=1.0)
    v_stag2 = complex_velocity(-1.0, U=1.0, R=1.0)
    assert np.isclose(v_stag1, 0.0)
    assert np.isclose(v_stag2, 0.0)
