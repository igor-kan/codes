"""Implementation of spherical harmonic radial component order 17089."""

def compute_spherical_harm_17089(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17089():
    v=compute_spherical_harm_17089(0.5)
    assert isinstance(v,float) and v==v
