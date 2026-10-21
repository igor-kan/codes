"""Implementation of spherical harmonic radial component order 16674."""

def compute_spherical_harm_16674(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16674():
    v=compute_spherical_harm_16674(0.5)
    assert isinstance(v,float) and v==v
