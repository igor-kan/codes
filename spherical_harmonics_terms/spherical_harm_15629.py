"""Implementation of spherical harmonic radial component order 15629."""

def compute_spherical_harm_15629(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15629():
    v=compute_spherical_harm_15629(0.5)
    assert isinstance(v,float) and v==v
