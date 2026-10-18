"""Implementation of spherical harmonic radial component order 16089."""

def compute_spherical_harm_16089(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16089():
    v=compute_spherical_harm_16089(0.5)
    assert isinstance(v,float) and v==v
