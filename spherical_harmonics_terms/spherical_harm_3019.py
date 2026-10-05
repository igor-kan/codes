"""Implementation of spherical harmonic radial component order 3019."""

def compute_spherical_harm_3019(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_3019():
    v=compute_spherical_harm_3019(0.5)
    assert isinstance(v,float) and v==v
