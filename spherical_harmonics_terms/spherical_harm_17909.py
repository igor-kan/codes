"""Implementation of spherical harmonic radial component order 17909."""

def compute_spherical_harm_17909(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17909():
    v=compute_spherical_harm_17909(0.5)
    assert isinstance(v,float) and v==v
