import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from wkb_approximation import wkb_bohr_sommerfeld_action

def test_harmonic_oscillator_action():
    # V(x) = 0.5 * m * w^2 * x^2, turning points at x = +- sqrt(2E / (m w^2))
    # Action integral int_{-a}^a p dx = pi * E / w
    m, w = 1.0, 1.0
    E = 2.5
    a = np.sqrt(2.0 * E / (m * w**2))
    action = wkb_bohr_sommerfeld_action(lambda x: 0.5 * m * w**2 * x**2, E, -a, a, m=m)
    expected = np.pi * E / w
    assert np.isclose(action, expected, atol=1e-2)
