import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kepler_orbit_solver import solve_kepler_elliptic, true_anomaly_from_eccentric, orbital_radius

def test_circular_orbit():
    # e = 0 -> M = E = nu
    M = 1.2
    E = solve_kepler_elliptic(M, e=0.0)
    assert np.isclose(E, M)
    nu = true_anomaly_from_eccentric(E, e=0.0)
    assert np.isclose(nu, M)
    r = orbital_radius(1.0, 0.0, nu)
    assert np.isclose(r, 1.0)

def test_perihelion_aphelion():
    a = 2.0
    e = 0.5
    r_peri = orbital_radius(a, e, nu=0.0)
    r_ap = orbital_radius(a, e, nu=np.pi)
    assert np.isclose(r_peri, a * (1 - e))
    assert np.isclose(r_ap, a * (1 + e))
