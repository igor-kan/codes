import numpy as np
from bohr_sommerfeld_quantization import bohr_sommerfeld_action


def test_bs_action():
    # Harmonic oscillator V(x) = 0.5 * x^2. Integral of sqrt(2*(2 - 0.5*x^2)) = sqrt(4 - x^2) from -2 to 2 is pi * R^2 / 2 = 2 * pi = pi * E
    E = 2.0
    V = lambda x: 0.5 * x**2
    a = bohr_sommerfeld_action(E, V, -2.0, 2.0)
    assert np.isclose(a, np.pi * E, rtol=0.01)
