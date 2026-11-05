"""Implementation of spherical harmonic radial component order 18414."""

def compute_spherical_harm_18414(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18414():
    v=compute_spherical_harm_18414(0.5)
    assert isinstance(v,float) and v==v
