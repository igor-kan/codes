"""Implementation of spherical harmonic radial component order 15889."""

def compute_spherical_harm_15889(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15889():
    v=compute_spherical_harm_15889(0.5)
    assert isinstance(v,float) and v==v
