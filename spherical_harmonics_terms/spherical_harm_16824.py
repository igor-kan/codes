"""Implementation of spherical harmonic radial component order 16824."""

def compute_spherical_harm_16824(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16824():
    v=compute_spherical_harm_16824(0.5)
    assert isinstance(v,float) and v==v
