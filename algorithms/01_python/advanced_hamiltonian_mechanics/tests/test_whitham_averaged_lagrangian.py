import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from whitham_averaged_lagrangian import linear_wave_averaged_lagrangian, wave_action_density

def test_dispersion_on_shell():
    # On shell omega = c k -> L_bar = 0
    L = linear_wave_averaged_lagrangian(omega=2.0, k=2.0, a=1.0, c=1.0)
    assert np.isclose(L, 0.0)
    J = wave_action_density(2.0, 1.5)
    assert np.isclose(J, 4.5)
