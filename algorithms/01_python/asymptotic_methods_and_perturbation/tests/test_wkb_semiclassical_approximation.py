import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from wkb_semiclassical_approximation import wkb_phase_integral

def test_free_particle_wkb():
    # V(x) = 0, E = 2.0 -> p = 2.0
    x = np.linspace(0, 1, 101)
    phase = wkb_phase_integral(lambda x: np.zeros_like(x), energy=2.0, x_grid=x, m=1.0)
    assert np.isclose(phase[-1], 2.0, rtol=1e-2)
