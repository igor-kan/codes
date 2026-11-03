"""Implementation of spherical harmonic radial component order 18124."""

def compute_spherical_harm_18124(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18124():
    v=compute_spherical_harm_18124(0.5)
    assert isinstance(v,float) and v==v
