import numpy as np
from quantum_harmonic_oscillator import qho_energy, qho_eigenfunction


def test_ground_state():
    x = np.linspace(-5, 5, 1001)
    dx = x[1] - x[0]
    psi0 = qho_eigenfunction(0, x)
    assert np.isclose(np.sum(psi0**2) * dx, 1.0, atol=1e-3)
    assert qho_energy(0, 2.0) == 1.0
    assert qho_energy(1, 2.0) == 3.0
