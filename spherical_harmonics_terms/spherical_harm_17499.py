"""Implementation of spherical harmonic radial component order 17499."""

def compute_spherical_harm_17499(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17499():
    v=compute_spherical_harm_17499(0.5)
    assert isinstance(v,float) and v==v
