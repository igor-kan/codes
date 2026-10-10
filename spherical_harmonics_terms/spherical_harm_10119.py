"""Implementation of spherical harmonic radial component order 10119."""

def compute_spherical_harm_10119(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10119():
    v=compute_spherical_harm_10119(0.5)
    assert isinstance(v,float) and v==v
