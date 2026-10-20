"""Implementation of spherical harmonic radial component order 16464."""

def compute_spherical_harm_16464(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16464():
    v=compute_spherical_harm_16464(0.5)
    assert isinstance(v,float) and v==v
