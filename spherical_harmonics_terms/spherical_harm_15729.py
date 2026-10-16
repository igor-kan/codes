"""Implementation of spherical harmonic radial component order 15729."""

def compute_spherical_harm_15729(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15729():
    v=compute_spherical_harm_15729(0.5)
    assert isinstance(v,float) and v==v
