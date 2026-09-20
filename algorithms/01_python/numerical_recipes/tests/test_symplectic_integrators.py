import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from symplectic_integrators import velocity_verlet_step, yoshida4_step

def test_harmonic_oscillator_energy():
    # V(q) = 0.5 * k * q^2 -> F(q) = -k * q
    k, m = 1.0, 1.0
    q, p = 1.0, 0.0
    dt = 0.1
    # Integrate 100 steps
    for _ in range(100):
        q, p = yoshida4_step(q, p, lambda x: -k * x, m, dt)
    energy = 0.5 * (p**2 / m + k * q**2)
    assert np.isclose(energy, 0.5, atol=1e-5)
