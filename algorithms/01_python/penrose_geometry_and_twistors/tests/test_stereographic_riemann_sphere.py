import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from stereographic_riemann_sphere import sphere_to_complex, complex_to_sphere

def test_stereographic_equator():
    # Points on equator z=0 map to unit circle |zeta| = 1
    c1 = sphere_to_complex(1.0, 0.0, 0.0)
    assert np.isclose(abs(c1), 1.0)
    assert np.isclose(c1.real, 1.0)
    
    # South pole (0, 0, -1) maps to origin 0
    c_south = sphere_to_complex(0.0, 0.0, -1.0)
    assert np.isclose(abs(c_south), 0.0)

def test_inverse_stereographic():
    pts = [(0.0, 0.0, -1.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
    for x, y, z in pts:
        zeta = sphere_to_complex(x, y, z)
        rx, ry, rz = complex_to_sphere(zeta)
        assert np.isclose(x, rx)
        assert np.isclose(y, ry)
        assert np.isclose(z, rz)
