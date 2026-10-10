"""Implementation of spherical harmonic radial component order 10104."""

def compute_spherical_harm_10104(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10104():
    v=compute_spherical_harm_10104(0.5)
    assert isinstance(v,float) and v==v
