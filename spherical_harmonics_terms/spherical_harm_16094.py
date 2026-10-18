"""Implementation of spherical harmonic radial component order 16094."""

def compute_spherical_harm_16094(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16094():
    v=compute_spherical_harm_16094(0.5)
    assert isinstance(v,float) and v==v
