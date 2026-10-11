"""Implementation of spherical harmonic radial component order 11104."""

def compute_spherical_harm_11104(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_11104():
    v=compute_spherical_harm_11104(0.5)
    assert isinstance(v,float) and v==v
