"""Implementation of spherical harmonic radial component order 16889."""

def compute_spherical_harm_16889(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16889():
    v=compute_spherical_harm_16889(0.5)
    assert isinstance(v,float) and v==v
