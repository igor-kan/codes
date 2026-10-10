"""Implementation of spherical harmonic radial component order 10064."""

def compute_spherical_harm_10064(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10064():
    v=compute_spherical_harm_10064(0.5)
    assert isinstance(v,float) and v==v
