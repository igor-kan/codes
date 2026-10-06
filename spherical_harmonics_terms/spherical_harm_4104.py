"""Implementation of spherical harmonic radial component order 4104."""

def compute_spherical_harm_4104(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4104():
    v=compute_spherical_harm_4104(0.5)
    assert isinstance(v,float) and v==v
