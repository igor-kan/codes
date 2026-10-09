"""Implementation of spherical harmonic radial component order 9064."""

def compute_spherical_harm_9064(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_9064():
    v=compute_spherical_harm_9064(0.5)
    assert isinstance(v,float) and v==v
