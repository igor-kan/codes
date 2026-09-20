import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from spherical_harmonics import spherical_harmonic

def test_y00_constant():
    # Y_0^0 = 1 / sqrt(4 pi)
    theta = np.linspace(0, np.pi, 20)
    phi = np.linspace(0, 2*np.pi, 20)
    y00 = spherical_harmonic(0, 0, theta, phi)
    expected = 1.0 / np.sqrt(4 * np.pi)
    assert np.allclose(y00, expected)

def test_orthonormality():
    # Integrate |Y_1^0|^2 sin(theta) dtheta dphi = 1
    t = np.linspace(0, np.pi, 100)
    p = np.linspace(0, 2*np.pi, 100)
    T, P = np.meshgrid(t, p)
    y10 = spherical_harmonic(1, 0, T, P)
    integral = np.trapezoid(np.trapezoid(np.abs(y10)**2 * np.sin(T), t, axis=1), p)
    assert np.isclose(integral, 1.0, atol=1e-2)
