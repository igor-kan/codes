import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lorentz_field_transform import transform_fields_boost_x

def test_lorentz_invariants():
    # Invariants: E^2 - c^2 B^2 and E . B
    c = 1.0
    E = np.array([1.0, 2.0, -1.0])
    B = np.array([0.5, -0.2, 1.5])
    inv1 = np.dot(E, E) - (c**2) * np.dot(B, B)
    inv2 = np.dot(E, B)

    E_p, B_p = transform_fields_boost_x(E, B, beta=0.6, c=c)
    inv1_p = np.dot(E_p, E_p) - (c**2) * np.dot(B_p, B_p)
    inv2_p = np.dot(E_p, B_p)

    assert np.isclose(inv1, inv1_p)
    assert np.isclose(inv2, inv2_p)
