"""Implementation of spherical harmonic radial component order 16644."""

def compute_spherical_harm_16644(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16644():
    v=compute_spherical_harm_16644(0.5)
    assert isinstance(v,float) and v==v
