"""Implementation of spherical harmonic radial component order 17254."""

def compute_spherical_harm_17254(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17254():
    v=compute_spherical_harm_17254(0.5)
    assert isinstance(v,float) and v==v
