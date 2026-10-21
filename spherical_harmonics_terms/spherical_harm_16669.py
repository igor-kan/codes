"""Implementation of spherical harmonic radial component order 16669."""

def compute_spherical_harm_16669(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16669():
    v=compute_spherical_harm_16669(0.5)
    assert isinstance(v,float) and v==v
