import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from euler_poinsot_elliptic import euler_poinsot_step_rk4

def test_poinsot_conservation_laws():
    I = np.array([1.0, 2.0, 3.0])
    w = np.array([1.0, 0.5, 0.2])
    E0 = 0.5 * np.sum(I * w**2)
    M2_0 = np.sum((I * w)**2)

    for _ in range(200):
        w = euler_poinsot_step_rk4(w, I, dt=0.01)

    Ef = 0.5 * np.sum(I * w**2)
    M2_f = np.sum((I * w)**2)
    assert np.isclose(Ef, E0, atol=1e-6)
    assert np.isclose(M2_f, M2_0, atol=1e-6)
