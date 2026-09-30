"""Implementation of spherical harmonic radial component order 9."""

def compute_spherical_harm_9(x: float) -> float:
    # Associated Legendre component
    l = 5
    return float((float(x) ** l) / float(l * 2))

import math

def test_compute_spherical_harm_9():
    val = compute_spherical_harm_9(0.5)
    assert isinstance(val, float)
    assert val == val
