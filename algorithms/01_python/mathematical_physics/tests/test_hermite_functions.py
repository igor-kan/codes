import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hermite_functions import hermite_polynomial, harmonic_oscillator_psi

def test_hermite_values():
    x = np.linspace(-2, 2, 50)
    # H_2(x) = 4x^2 - 2
    assert np.allclose(hermite_polynomial(2, x), 4 * x**2 - 2)

def test_wavefunction_normalization():
    x = np.linspace(-8, 8, 2000)
    psi0 = harmonic_oscillator_psi(0, x)
    psi1 = harmonic_oscillator_psi(1, x)
    assert np.isclose(np.trapezoid(psi0**2, x), 1.0, atol=1e-3)
    assert np.isclose(np.trapezoid(psi1**2, x), 1.0, atol=1e-3)
    assert np.isclose(np.trapezoid(psi0 * psi1, x), 0.0, atol=1e-4)
