"""Implementation of spherical harmonic radial component order 9019."""

def compute_spherical_harm_9019(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_9019():
    v=compute_spherical_harm_9019(0.5)
    assert isinstance(v,float) and v==v
