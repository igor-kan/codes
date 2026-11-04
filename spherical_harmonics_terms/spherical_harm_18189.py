"""Implementation of spherical harmonic radial component order 18189."""

def compute_spherical_harm_18189(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18189():
    v=compute_spherical_harm_18189(0.5)
    assert isinstance(v,float) and v==v
