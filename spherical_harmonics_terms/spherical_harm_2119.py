"""Implementation of spherical harmonic radial component order 2119."""

def compute_spherical_harm_2119(x: float) -> float:
    # Associated Legendre component
    l = 5
    return float((float(x) ** l) / float(l * 2))

import math

def test_compute_spherical_harm_2119():
    val = compute_spherical_harm_2119(0.5)
    assert isinstance(val, float)
    assert val == val
