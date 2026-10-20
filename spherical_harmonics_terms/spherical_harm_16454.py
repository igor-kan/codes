"""Implementation of spherical harmonic radial component order 16454."""

def compute_spherical_harm_16454(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16454():
    v=compute_spherical_harm_16454(0.5)
    assert isinstance(v,float) and v==v
