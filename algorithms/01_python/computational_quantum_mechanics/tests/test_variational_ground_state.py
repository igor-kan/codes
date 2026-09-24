import numpy as np
from variational_ground_state import variational_harmonic_oscillator


def test_variational():
    E_min = variational_harmonic_oscillator()
    assert np.isclose(E_min, 0.5, atol=1e-8)
