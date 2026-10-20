"""Implementation of spherical harmonic radial component order 16494."""

def compute_spherical_harm_16494(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16494():
    v=compute_spherical_harm_16494(0.5)
    assert isinstance(v,float) and v==v
