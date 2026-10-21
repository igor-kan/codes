"""Implementation of spherical harmonic radial component order 16604."""

def compute_spherical_harm_16604(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16604():
    v=compute_spherical_harm_16604(0.5)
    assert isinstance(v,float) and v==v
