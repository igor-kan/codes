import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from brachistochrone_variational import cycloid_coordinates, descent_time

def test_cycloid_points():
    theta = np.linspace(0, 2*np.pi, 50)
    x, y = cycloid_coordinates(theta, 1.0)
    assert x[0] == 0.0 and y[0] == 0.0
    assert np.isclose(x[-1], 2 * np.pi)
    assert np.isclose(y[-1], 0.0)
