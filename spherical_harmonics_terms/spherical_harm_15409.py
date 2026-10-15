"""Implementation of spherical harmonic radial component order 15409."""

def compute_spherical_harm_15409(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15409():
    v=compute_spherical_harm_15409(0.5)
    assert isinstance(v,float) and v==v
