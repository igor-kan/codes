import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from poiseuille_couette_flow import plane_poiseuille_velocity, planar_couette_velocity

def test_poiseuille_profile():
    y = np.linspace(0, 1.0, 11)
    u = plane_poiseuille_velocity(y, h=1.0, dp_dx=-2.0, mu=1.0)
    # Maximum velocity at centerline y = 0.5: u_max = (-dp/dx) h^2 / (8 mu) = 2 / 8 = 0.25
    assert np.isclose(u[5], 0.25)
    assert np.isclose(u[0], 0.0)
    assert np.isclose(u[-1], 0.0)
