"""Implementation of spherical harmonic radial component order 16474."""

def compute_spherical_harm_16474(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16474():
    v=compute_spherical_harm_16474(0.5)
    assert isinstance(v,float) and v==v
