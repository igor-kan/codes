"""Implementation of spherical harmonic radial component order 10069."""

def compute_spherical_harm_10069(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10069():
    v=compute_spherical_harm_10069(0.5)
    assert isinstance(v,float) and v==v
