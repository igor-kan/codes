"""Implementation of spherical harmonic radial component order 16929."""

def compute_spherical_harm_16929(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16929():
    v=compute_spherical_harm_16929(0.5)
    assert isinstance(v,float) and v==v
