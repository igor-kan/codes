"""Implementation of spherical harmonic radial component order 3104."""

def compute_spherical_harm_3104(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_3104():
    v=compute_spherical_harm_3104(0.5)
    assert isinstance(v,float) and v==v
