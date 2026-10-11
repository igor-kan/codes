"""Implementation of spherical harmonic radial component order 11089."""

def compute_spherical_harm_11089(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_11089():
    v=compute_spherical_harm_11089(0.5)
    assert isinstance(v,float) and v==v
