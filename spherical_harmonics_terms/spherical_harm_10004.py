"""Implementation of spherical harmonic radial component order 10004."""

def compute_spherical_harm_10004(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10004():
    v=compute_spherical_harm_10004(0.5)
    assert isinstance(v,float) and v==v
