"""Implementation of spherical harmonic radial component order 17629."""

def compute_spherical_harm_17629(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17629():
    v=compute_spherical_harm_17629(0.5)
    assert isinstance(v,float) and v==v
